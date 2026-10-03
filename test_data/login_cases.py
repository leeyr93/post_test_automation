from utils.constants import UIErrorMsg
from utils import user

LOGIN_INVALID_CASES = [
    {
        "name": "empty_both",
        "tc_id": "TC-23",
        "tc_title": "아이디 및 비밀번호 미입력 시 에러 메시지 노출 확인",
        "data": {"id": "", "password": ""},
        "expected": {"message": UIErrorMsg.LOGIN_EMPTY_BOTH}
    },
    {
        "name": "empty_id",
        "tc_id": "TC-24",
        "tc_title": "아이디 미입력 시 에러 메시지 노출 확인",
        "data": {"id": "", "password": "testpassword"},
        "expected": {"message": UIErrorMsg.LOGIN_EMPTY_ID}
    },
    {
        "name": "empty_password",
        "tc_id": "TC-25",
        "tc_title": "비밀번호 미입력 시 에러 메시지 노출 확인",
        "data": {"id": "test1", "password": ""},
        "expected": {"message": UIErrorMsg.LOGIN_EMPTY_PASSWORD}
    },
    {
        "name": "unknown_user",
        "tc_id": "TC-26",
        "tc_title": "미등록 계정 정보로 로그인 시도시 에러 메시지 노출 확인",
        "data": {"id": "unknown_user_123", "password": "wrongpassword123!"},
        "expected": {"message": UIErrorMsg.LOGIN_UNKNOWN_USER}
    },
    {
        "name": "wrong_password",
        "tc_id": "TC-27",
        "tc_title": "잘못된 비밀번호 입력 시 에러 메시지 노출 확인",
        "data": {"id": user.ID, "password": "wrongpassword123!"},
        "expected": {"message": UIErrorMsg.LOGIN_WRONG_PASSWORD}
    }
]
