import unittest
import json
from api_client import PetstoreAPIClient

class TestPetstoreAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Загружаем конфигурацию один раз перед всеми тестами
        try:
            with open("config.json", "r") as f:
                cls.config = json.load(f)
        except FileNotFoundError:
            cls.config = {}
            print("Предупреждение: Файл config.json не найден. Используются значения по умолчанию.")
        cls.client = PetstoreAPIClient()

    def test_get_pets_by_status(self):
        """Тест получения списка доступных питомцев."""
        response = self.client.get_pets_by_status("available")
        self.assertEqual(response.status_code, 200, "Ожидался код 200")
        data = response.json()
        self.assertIsInstance(data, list, "Ожидался список питомцев")
        self.assertTrue(all(pet["status"] == "available" for pet in data), "Не все питомцы имеют статус 'available'")

    def test_add_pet(self):
        """Тест добавления нового питомца."""
        pet_data = self.config.get("test_pet", {
            "id": 12345,
            "name": "Fluffy",
            "status": "available"
        })
        response = self.client.add_pet(pet_data)
        self.assertEqual(response.status_code, 200, "Ожидался код 200")
        data = response.json()
        self.assertEqual(data["name"], pet_data["name"], "Имя питомца не совпадает")

    def test_update_pet(self):
        """Тест обновления данных питомца."""
        updated_pet_data = self.config.get("updated_pet", {
            "id": 12345,
            "name": "FluffyUpdated",
            "status": "sold"
        })
        response = self.client.update_pet(updated_pet_data)
        self.assertEqual(response.status_code, 200, "Ожидался код 200")
        data = response.json()
        self.assertEqual(data["name"], updated_pet_data["name"], "Обновленное имя не совпадает")
        self.assertEqual(data["status"], "sold", "Статус не обновился")

    def test_delete_pet(self):
        """Тест удаления питомца."""
        pet_id = self.config.get("test_pet", {}).get("id", 12345)
        response = self.client.delete_pet(pet_id)
        self.assertEqual(response.status_code, 200, "Ожидался код 200")
        # Проверка, что питомец удален
        check_response = self.client.get_pet_by_id(pet_id)
        self.assertEqual(check_response.status_code, 404, "Питомец не был удален")

    def test_get_non_existent_pet(self):
        """Тест запроса несуществующего питомца."""
        pet_id = self.config.get("non_existent_pet_id", 99999)
        response = self.client.get_pet_by_id(pet_id)
        self.assertEqual(response.status_code, 404, "Ожидался код 404")
        data = response.json()
        self.assertIn("message", data, "Сообщение об ошибке отсутствует")

if __name__ == "__main__":
    unittest.main(argv=['-v'])