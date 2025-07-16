import configuration
import data
import sender_stand_request


def get_kit_body(name):
    return {"name": name}

# Tests positivos
def positive_assert(kit_body):
    token = get_new_user_token()
    response = post_new_client_kit(kit_body.copy(), token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Tests negativos
def negative_assert_code_400(kit_body):
    token = get_new_user_token()
    response = post_new_client_kit(kit_body.copy(), token)
    assert response.status_code == 400

# Tests individuales
def test_kit_name_1_char():
    positive_assert(kit_body_1_char)

def test_kit_name_511_chars():
    positive_assert(kit_body_511_chars)

def test_kit_name_empty():
    negative_assert_code_400(kit_body_empty)

def test_kit_name_512_chars():
    negative_assert_code_400(kit_body_512_chars)

def test_kit_name_special_chars():
    positive_assert(kit_body_special_chars)

def test_kit_name_spaces():
    positive_assert(kit_body_spaces)

def test_kit_name_numbers():
    positive_assert(kit_body_numbers)

def test_kit_name_missing_name():
    negative_assert_code_400(kit_body_missing_name)

def test_kit_name_wrong_type():
    negative_assert_code_400(kit_body_wrong_type)