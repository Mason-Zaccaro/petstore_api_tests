import requests
import json

class PetstoreAPIClient:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as f:
            config = json.load(f)
        self.BASE_URL = config["base_url"]
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json", "accept": "application/json"})

    def get_pets_by_status(self, status):
        url = f"{self.BASE_URL}/pet/findByStatus"
        params = {"status": status}
        response = self.session.get(url, params=params)
        return response

    def add_pet(self, pet_data):
        url = f"{self.BASE_URL}/pet"
        response = self.session.post(url, json=pet_data)
        return response

    def update_pet(self, pet_data):
        url = f"{self.BASE_URL}/pet"
        response = self.session.put(url, json=pet_data)
        return response

    def delete_pet(self, pet_id):
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.delete(url)
        return response

    def get_pet_by_id(self, pet_id):
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.get(url)
        return response