# Find ID test data cases
FIND_ID_INVALID_CASES = [
    {
        "name": "nonexistent_user",
        "data": {"name": "없는사용자", "email": "nonexistent@test.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "name_only",
        "data": {"name": "홍길동", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "email_only",
        "data": {"name": "", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_fields",
        "data": {"name": "", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "mismatched_email",
        "data": {"name": "홍길동", "email": "wrong_email@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    }
]

# Find PW test data cases
FIND_PW_INVALID_CASES = [
    {
        "name": "nonexistent_user_id",
        "data": {"user_id": "nonexistent_user", "name": "홍길동", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "mismatched_name",
        "data": {"user_id": "validuser", "name": "틀린이름", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "mismatched_email",
        "data": {"user_id": "validuser", "name": "홍길동", "email": "wrong@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_user_id",
        "data": {"user_id": "", "name": "홍길동", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_name",
        "data": {"user_id": "validuser", "name": "", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_email",
        "data": {"user_id": "validuser", "name": "홍길동", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "empty_fields",
        "data": {"user_id": "", "name": "", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    }
]

# Reset PW test data cases
RESET_PW_INVALID_CASES = [
    {
        "name": "password_mismatch",
        "data": {"password": "NewPassword123!", "repassword": "DifferentPassword123!"},
        "expected": {"message": "비밀번호가 일치하지 않습니다."}
    }
]

