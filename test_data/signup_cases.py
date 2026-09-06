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
        "tc_id": "TC-13",
        "tc_title": "유효한 정보로 가입 성공 및 화면 이동 확인",
        "data": get_valid_user_data(),
        "expected": {"redirect": "/login"}
    }


INVALID_CASES = [
    {
        "name": "invalid_password_length",
        "tc_id": "TC-07",
        "tc_title": "비밀번호 길이 제한 미달 시(8자 미만) 가입 불가 확인",
        "override": {"password": "123", "repassword": "123"},
        "expected": {
            "message": "비밀번호는 '영문, 숫자, 특수문자 조합. 8-16자' 형식에 맞게 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "invalid_password_match",
        "tc_id": "TC-08",
        "tc_title": "비밀번호와 비밀번호 확인 불일치 시 가입 불가 확인",
        "override": {"repassword": "Different123!"},
        "expected": {
            "message": "비밀번호가 일치하지 않습니다.",
            "reset": True
        }
    },
    {
        "name": "invalid_name_format",
        "tc_id": "TC-09",
        "tc_title": "이름 형식 위반(숫자 포함) 시 가입 불가 확인",
        "override": {"name": "홍길동123"},
        "expected": {
            "message": "이름은 '숫자, 특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "invalid_email_format",
        "tc_id": "TC-10",
        "tc_title": "잘못된 이메일 형식 입력 시 가입 불가 확인",
        "override": {"email": "wrong-email"},
        "expected": {
            "message": "이메일은 '예) example@gmail.com' 형식에 맞게 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "empty_user_id",
        "tc_id": "TC-11",
        "tc_title": "아이디 미입력 상태 가입 시도시 차단 확인",
        "override": {"user_id": ""},
        "expected": {
            "message": "아이디를 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "duplicate_user_id",
        "tc_id": "TC-12",
        "tc_title": "중복된 아이디로 가입 시도시 차단 확인",
        "override": {"user_id": "yllee"},   # 실제 DB에 존재하는 아이디
        "expected": {
            "message": "사용중인 아이디입니다."
        }
    }
]