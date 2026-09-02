# Find ID test data cases
FIND_ID_INVALID_CASES = [
    {
        "name": "존재하지 않는 사용자 정보",
        "data": {"name": "없는사용자", "email": "nonexistent@test.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "이름만 입력",
        "data": {"name": "홍길동", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "이메일만 입력",
        "data": {"name": "", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "모두 빈 값 입력",
        "data": {"name": "", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "이메일 불일치",
        "data": {"name": "홍길동", "email": "wrong_email@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    }
]

# Find PW test data cases
FIND_PW_INVALID_CASES = [
    {
        "name": "존재하지 않는 아이디",
        "data": {"user_id": "nonexistent_user", "name": "홍길동", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "이름 불일치",
        "data": {"user_id": "validuser", "name": "틀린이름", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "이메일 불일치",
        "data": {"user_id": "validuser", "name": "홍길동", "email": "wrong@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "아이디 미입력",
        "data": {"user_id": "", "name": "홍길동", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "이름 미입력",
        "data": {"user_id": "validuser", "name": "", "email": "test@gmail.com"},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "이메일 미입력",
        "data": {"user_id": "validuser", "name": "홍길동", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    },
    {
        "name": "모두 빈 값 입력",
        "data": {"user_id": "", "name": "", "email": ""},
        "expected": {"message": "일치하는 정보가 없습니다."}
    }
]

# Reset PW test data cases
RESET_PW_INVALID_CASES = [
    {
        "name": "비밀번호와 비밀번호 확인 불일치",
        "data": {"password": "NewPassword123!", "repassword": "DifferentPassword123!"},
        "expected": {"message": "비밀번호가 일치하지 않습니다."}
    }
]
