from http.client import responses

import allure_pytest.plugin
import requests
import allure

BASE_URL = "https://petstore.swagger.io/v2/pet"

class PetStoreAPI:

    @allure.step("Добавление нового питомца")
    def add_pet(self, new_pet):
        response = requests.post(BASE_URL, json=new_pet)
        response_data = response.json()
        assert response_data["id"] == new_pet["id"], "ID питомца не совпадает"
        assert response_data["name"] == new_pet["name"], "Имя питомца не совпадает"
        print("\n")
        print(f"Питомец добавлен:      {response_data}")
        return response_data

    @allure.step("Проверка, что питомец добавлен")
    def verify_pet_exists(self, pet_id, expected_name):
        response = requests.get(f"{BASE_URL}/{pet_id}")
        response_data = response.json()
        assert response_data["id"] == pet_id, "ID не совпадает"
        assert response_data["name"] == expected_name, "Имя не совпадает"
        print(f"Питомец найден:        {response_data}")

    @allure.step("Обновление питомца")
    def update_pet_name(self, pet, new_name):
        updated_pet = pet.copy()
        updated_pet["name"] = new_name
        response = requests.put(BASE_URL, json=updated_pet)
        response.data = response.json()
        assert response.data['name'] == new_name, "Имя не обновлено"
        assert  response.data['id'] == updated_pet['id'], "id не совпадает"
        print(f"Имя питомца обновлено: {response.data}")
        return response.data

    @allure.step("Удаление питомца")
    def delete_pet(self, pet_id):
        response = requests.delete(f"{BASE_URL}/{pet_id}")
        assert response.status_code == 200, f"Ошибка при удалении питомца: {response.text}"
        print(f"Питомец с ID {pet_id} удалён")
        print("\n")

    @allure.step("Проверка, что питомец удалён")
    def verify_pet_deleted(self, pet_id, pet_name):
        response = requests.get(f"{BASE_URL}/{pet_id}")
        response_data = response.json()
        assert response_data["message"] == "Pet not found", "Сообщение об ошибке некорректно"

