# Find ID test data cases
FIND_ID_INVALID_CASES = [
    {
        "name": "nonexistent_user",
        "tc_id": "TC-16",
        "tc_title": "미등록 사용자 정보 입력 시 실패 메시지 확인",
        "data": {"name": "없는사용자", "email": "nonexistent@test.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "name_only",
        "tc_id": "TC-17",
        "tc_title": "이름만 입력하고 이메일 미입력 시 실패 확인",
        "data": {"name": "홍길동", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "email_only",
        "tc_id": "TC-18",
        "tc_title": "이메일만 입력하고 이름 미입력 시 실패 확인",
        "data": {"name": "", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_fields",
        "tc_id": "TC-19",
        "tc_title": "필드 전체 미입력 시 실패 메시지 확인",
        "data": {"name": "", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "mismatched_email",
        "tc_id": "TC-20",
        "tc_title": "가입된 이름에 불일치 이메일 입력 시 실패 확인",
        "data": {"name": "홍길동", "email": "wrong_email@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    }
]

# Find PW test data cases
FIND_PW_INVALID_CASES = [
    {
        "name": "nonexistent_user_id",
        "tc_id": "TC-29",
        "tc_title": "미등록 아이디 입력 시 실패 메시지 확인",
        "data": {"user_id": "nonexistent_user", "name": "홍길동", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "mismatched_name",
        "tc_id": "TC-30",
        "tc_title": "등록된 아이디에 불일치 이름 입력 시 실패 확인",
        "data": {"user_id": "validuser", "name": "틀린이름", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "mismatched_email",
        "tc_id": "TC-31",
        "tc_title": "등록된 아이디에 불일치 이메일 입력 시 실패 확인",
        "data": {"user_id": "validuser", "name": "홍길동", "email": "wrong@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_user_id",
        "tc_id": "TC-32",
        "tc_title": "아이디 미입력 시 실패 확인",
        "data": {"user_id": "", "name": "홍길동", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_name",
        "tc_id": "TC-33",
        "tc_title": "이름 미입력 시 실패 확인",
        "data": {"user_id": "validuser", "name": "", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_email",
        "tc_id": "TC-34",
        "tc_title": "이메일 미입력 시 실패 확인",
        "data": {"user_id": "validuser", "name": "홍길동", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_fields",
        "tc_id": "TC-35",
        "tc_title": "전체 항목 미입력 시 실패 확인",
        "data": {"user_id": "", "name": "", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    }
]

# Reset PW test data cases
RESET_PW_INVALID_CASES = [
    {
        "name": "password_mismatch",
        "tc_id": "TC-38",
        "tc_title": "신규 비밀번호와 재입력 불일치 시 차단 확인",
        "data": {"password": "NewPassword123!", "repassword": "DifferentPassword123!"},
        "expected": {"message": "비밀번호가 일치하지 않습니다."}
    }
]
