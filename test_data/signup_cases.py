from utils.random_generator import generate_random_user_id

BASE_VALID_DATA = {
    "user_id": "validuser",
    "password": "Valid123!",
    "repassword": "Valid123!",
    "name": "홍길동",
    "email": "test@gmail.com"
}


def valid_signup_case():
    data = BASE_VALID_DATA.copy()
    data["user_id"] = generate_random_user_id()
    return {
        "name": "성공 케이스",
        "data": data,
        "expected": {"redirect": "/login"}
    }


INVALID_CASES = [
    {
        "name": "비밀번호 짧음",
        "override": {"password": "123", "repassword": "123"},
        "expected": {
            "message": "비밀번호는 '영문, 숫자, 특수문자 조합. 8-16자' 형식에 맞게 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "비밀번호 불일치",
        "override": {"repassword": "Different123!"},
        "expected": {
            "message": "비밀번호가 일치하지 않습니다.",
            "reset": True
        }
    },
    {
        "name": "이름 형식 오류",
        "override": {"name": "홍길동123"},
        "expected": {
            "message": "이름은 '숫자, 특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "이메일 형식 오류",
        "override": {"email": "wrong-email"},
        "expected": {
            "message": "이메일은 '예) example@gmail.com' 형식에 맞게 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "아이디 미입력",
        "override": {"user_id": ""},
        "expected": {
            "message": "아이디를 입력해주세요.",
            "reset": True
        }
    },
    {
        "name": "중복 아이디",
        "override": {"user_id": "yllee"},   # 실제 DB에 존재하는 아이디로 변경
        "expected": {
            "message": "사용중인 아이디입니다."
        }
    }
]