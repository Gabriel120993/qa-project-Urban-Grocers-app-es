kit_name_1_char = {"name": "a"}
kit_name_511_chars = {"name": "a" * 511}
kit_name_special_chars = {"name": "№%@,"}
kit_name_spaces = {"name": " A Aaa "}
kit_name_numbers = {"name": "123"}

# Casos inválidos
kit_name_empty = {"name": ""}
kit_name_512_chars = {"name": "a" * 512}
kit_name_missing = {}
kit_name_number_type = {"name": 123}

def post_new_user():
    user_body = {
        "firstName": "Juan",
        "phone": "+12345678901",
        "address": "Calle Falsa 123"
    }
    response = requests.post(URL_SERVICE + CREATE_USER_PATH, json=user_body)
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(URL_SERVICE + CREATE_KIT_PATH, headers=headers, json=kit_body)
    return response