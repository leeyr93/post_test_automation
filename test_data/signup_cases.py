import copy
import uuid
from utils import user

BASE_VALID_DATA = {
    "user_id": "testuser1",
    "password": "test1!234",
    "repassword": "test1!234",
    "name": "홍길동",
    "email": "test@gmail.com"
}

INVALID_CASES = [
    {
        "name": "empty_all_fields",
        "tc_id": "TC-02",
        "tc_title": "전체 입력 필드 미입력 시 에러 메시지 노출 확인",
        "override": {
            "user_id": "",
            "password": "",
            "repassword": "",
            "name": "",
            "email": ""
        },
        "expected": {"message": "아이디를 입력해주세요.", "reset": True}
    },
    {
        "name": "empty_user_id",
        "tc_id": "TC-03",
        "tc_title": "아이디 미입력 시 에러 메시지 노출 확인",
        "override": {"user_id": ""},
        "expected": {"message": "아이디를 입력해주세요.", "reset": True}
    },
    {
        "name": "user_id_only_alpha",
        "tc_id": "TC-04",
        "tc_title": "아이디 영문만 입력 시 에러 메시지 노출 확인",
        "override": {"user_id": "onlyalpha"},
        "expected": {"message": "아이디는 '특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "user_id_only_num",
        "tc_id": "TC-05",
        "tc_title": "아이디 숫자만 입력 시 에러 메시지 노출 확인",
        "override": {"user_id": "99887766"},
        "expected": {"message": "아이디는 '특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "user_id_special_char",
        "tc_id": "TC-06",
        "tc_title": "아이디 특수문자 포함 입력 시 에러 메시지 노출 확인",
        "override": {"user_id": "test!123"},
        "expected": {"message": "아이디는 '특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "user_id_too_long",
        "tc_id": "TC-07",
        "tc_title": "아이디 10자 초과 입력 시 에러 메시지 노출 확인",
        "override": {"user_id": "a1234567890"},
        "expected": {"message": "아이디는 '특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "empty_password",
        "tc_id": "TC-08",
        "tc_title": "비밀번호 미입력 시 에러 메시지 노출 확인",
        "override": {"password": ""},
        "expected": {"message": "비밀번호를 입력해주세요.", "reset": True}
    },
    {
        "name": "empty_repassword",
        "tc_id": "TC-09",
        "tc_title": "비밀번호 확인 필드 미입력 시 에러 메시지 노출 확인",
        "override": {"repassword": ""},
        "expected": {"message": "비밀번호를 재입력해주세요.", "reset": True}
    },
    {
        "name": "password_only_alpha",
        "tc_id": "TC-10",
        "tc_title": "비밀번호 영문만 입력 시 에러 메시지 노출 확인",
        "override": {"password": "testpassword", "repassword": "testpassword"},
        "expected": {"message": "비밀번호는 '영문, 숫자, 특수문자 조합. 8-16자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "password_only_num",
        "tc_id": "TC-11",
        "tc_title": "비밀번호 숫자만 입력 시 에러 메시지 노출 확인",
        "override": {"password": "12345678", "repassword": "12345678"},
        "expected": {"message": "비밀번호는 '영문, 숫자, 특수문자 조합. 8-16자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "password_too_short",
        "tc_id": "TC-12",
        "tc_title": "비밀번호 8자 미만 입력 시 에러 메시지 노출 확인",
        "override": {"password": "test1!", "repassword": "test1!"},
        "expected": {"message": "비밀번호는 '영문, 숫자, 특수문자 조합. 8-16자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "password_too_long",
        "tc_id": "TC-13",
        "tc_title": "비밀번호 16자 초과 입력 시 에러 메시지 노출 확인",
        "override": {"password": "test1!12345678901", "repassword": "test1!12345678901"},
        "expected": {"message": "비밀번호는 '영문, 숫자, 특수문자 조합. 8-16자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "password_mismatch",
        "tc_id": "TC-14",
        "tc_title": "비밀번호와 비밀번호 확인 불일치 시 에러 메시지 노출 확인",
        "override": {"password": "test1!234", "repassword": "WrongPassword123!"},
        "expected": {"message": "비밀번호가 일치하지 않습니다.", "reset": True}
    },
    {
        "name": "empty_name",
        "tc_id": "TC-15",
        "tc_title": "이름 미입력 시 에러 메시지 노출 확인",
        "override": {"name": ""},
        "expected": {"message": "이름을 입력해주세요.", "reset": True}
    },
    {
        "name": "name_with_number",
        "tc_id": "TC-16",
        "tc_title": "이름에 숫자 포함 시 에러 메시지 노출 확인",
        "override": {"name": "홍길동1"},
        "expected": {"message": "이름은 '숫자, 특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "name_with_special_char",
        "tc_id": "TC-17",
        "tc_title": "이름에 특수문자 포함 시 에러 메시지 노출 확인",
        "override": {"name": "홍길동!"},
        "expected": {"message": "이름은 '숫자, 특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "name_too_long",
        "tc_id": "TC-18",
        "tc_title": "이름 10자 초과 입력 시 에러 메시지 노출 확인",
        "override": {"name": "가나다라마바사아자차카"},
        "expected": {"message": "이름은 '숫자, 특수문자를 제외한 문자 조합. 1-10자' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "empty_email",
        "tc_id": "TC-19",
        "tc_title": "이메일 미입력 시 에러 메시지 노출 확인",
        "override": {"email": ""},
        "expected": {"message": "이메일을 입력해주세요.", "reset": True}
    },
    {
        "name": "email_no_at",
        "tc_id": "TC-20",
        "tc_title": "이메일 @ 미포함 형식 입력 시 에러 메시지 노출 확인",
        "override": {"email": "testgmail.com"},
        "expected": {"message": "이메일은 '예) example@gmail.com' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "email_no_domain",
        "tc_id": "TC-21",
        "tc_title": "이메일 도메인 미포함 형식 입력 시 에러 메시지 노출 확인",
        "override": {"email": "test@"},
        "expected": {"message": "이메일은 '예) example@gmail.com' 형식에 맞게 입력해주세요.", "reset": True}
    },
    {
        "name": "duplicate_user_id",
        "tc_id": "TC-23",
        "tc_title": "중복된 아이디로 가입 시도시 에러 메시지 노출 확인",
        "override": {"user_id": user.ID_TEMP}, 
        "expected": {"message": "사용중인 아이디입니다.", "reset": True}
    }
]

def get_valid_user_data(**overrides):
    data = copy.deepcopy(BASE_VALID_DATA)
    # 아이디는 기본적으로 랜덤생성 (중복 방지 및 _ 미포함)
    data["user_id"] = f"test1{uuid.uuid4().hex[:5]}"
    data.update(overrides)
    return data
