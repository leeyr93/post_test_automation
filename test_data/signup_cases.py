from utils.random_generator import generate_random_user_id

BASE_VALID_DATA = {
    "user_id": "validuser",
    "password": "valid123!",
    "repassword": "valid123!",
    "name": "홍길동",
    "email": "test@gmail.com"
}


def get_valid_user_data(**overrides) -> dict:
    data = BASE_VALID_DATA.copy()
    user_id = overrides.get("user_id", generate_random_user_id())
    data["user_id"] = user_id
    data["email"] = overrides.get("email", f"{user_id}@gmail.com")
    data.update(overrides)
    return data


def valid_signup_case():
    return {
        "name": "success",
        "data": get_valid_user_data(),
        "expected": {"redirect": "/login"}
    }




INVALID_CASES = [
    {
        "name": "invalid_password_length",
        "override": {"password": "123", "repassword": "123"},
        "expected": {
            "message": "비밀번호는 '영문, 숫자, 특수문자 조합. 8-16자' 형식에 맞게 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "invalid_password_match",
        "override": {"repassword": "Different123!"},
        "expected": {
            "message": "비밀번호가 일치하지 않습니다.",
            "reset": True
        }
    },
    {
        "name": "invalid_name_format",
        "override": {"name": "홍길동123"},
        "expected": {
            "message": "이름은 '숫자, 특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "invalid_email_format",
        "override": {"email": "wrong-email"},
        "expected": {
            "message": "이메일은 '예) example@gmail.com' 형식에 맞게 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "empty_user_id",
        "override": {"user_id": ""},
        "expected": {
            "message": "아이디를 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "duplicate_user_id",
        "override": {"user_id": "yllee"},   # 실제 DB에 존재하는 아이디
        "expected": {
            "message": "사용중인 아이디입니다."
        }
    }
]