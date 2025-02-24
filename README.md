# Petstore API Tests

Этот проект содержит автоматизированные тесты для API Petstore (https://petstore.swagger.io/), разработанные для проверки основных функций работы с питомцами (GET, POST, PUT, DELETE). Тесты написаны на Python с использованием библиотеки `requests` и фреймворка `pytest`.

## Описание проекта
Проект тестирует CRUD-операции API:
- **GET**: получение информации о питомце по ID.
- **POST**: создание нового питомца.
- **PUT**: обновление данных питомца.
- **DELETE**: удаление питомца.

Выбор методов обоснован задачей проверки всех основных операций, предоставляемых API Petstore. 
GET используется для чтения данных, 
POST — для создания, 
PUT — для изменения, 
DELETE — для удаления.

## Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Mason-Zaccaro/petstore_api_tests.git
   cd petstore_api_tests
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
3. Запустите тесты:
   ```bash
   python main.py
   
## Документация:
— [TEST_SCENARIOS.md](/TEST_SCENARIOS.md) описание сценариев и ожидаемых результатов. 
— [REPORT.md](/REPORT.md) результаты тестов и выводы о состоянии API. 

## Требования
Python 3.8+ 
Библиотеки: requests, pytest