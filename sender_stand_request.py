import requests
import configuration
import data


def get_new_user_token():
    user_body = {
        "firstName": "Juan",
        "phone": "+12345678901",
        "address": "Calle Falsa 123"
    }
    response = requests.post(URL_SERVICE + CREATE_USER_PATH, json=user_body)
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.post(URL_SERVICE + CREATE_KIT_PATH, headers=headers, json=kit_body)
    return response
