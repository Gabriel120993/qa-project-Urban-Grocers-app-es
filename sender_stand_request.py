import requests
import configuration

def post_new_user():
    user_body = {
        "firstName": "Gabriel",
        "phone": "+12345678901",
        "address": "Calle Falsa 123"
    }
    response = requests.post(URL_SERVICE + CREATE_USER_PATH, json=user_body)
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(URL_SERVICE + CREATE_KIT_PATH, headers=headers, json=kit_body)
