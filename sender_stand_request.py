import configuration
import requests
import data

# Crear usuario y obtener authToken
def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body)

def get_new_user_token():
    response = post_new_user()
    return response.json()["authToken"]

# Crear kit usando el token
def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body, headers=headers)
