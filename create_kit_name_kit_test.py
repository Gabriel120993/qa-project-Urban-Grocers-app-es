import data
from sender_stand_request import post_new_user, post_new_client_kit

# Función que genera el cuerpo del kit con nombre dinámico
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Función para pruebas positivas
def positive_assert(kit_body):
    token = post_new_user()
    response = post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Función para pruebas negativas (espera código 400)
def negative_assert_code_400(kit_body):
    token = post_new_user()
    response = post_new_client_kit(kit_body, token)
    assert response.status_code == 400

# Pruebas positivas

def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("g")
    positive_assert(kit_body)

def test_create_kit_511_letters_in_name_get_success_response():
    kit_body = {"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    positive_assert(kit_body)

def test_create_kit_special_characters_in_name_get_success_response():
    kit_body = get_kit_body("№%@,")
    positive_assert(kit_body)

def test_create_kit_name_with_spaces_get_success_response():
    kit_body = get_kit_body(" G Bernabe ")
    positive_assert(kit_body)

def test_create_kit_name_with_numbers_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

# Pruebas negativas

def test_create_kit_empty_name_get_error_400():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

def test_create_kit_512_letters_in_name_get_error_400():
    kit_body = {"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    negative_assert_code_400(kit_body)

def test_create_kit_without_name_get_error_400():
    token = post_new_user()
    response = post_new_client_kit({}, token)
    assert response.status_code == 400

def test_create_kit_number_as_name_get_error_400():
    token = post_new_user()
    response = post_new_client_kit({"name": 123}, token)
    assert response.status_code == 400
