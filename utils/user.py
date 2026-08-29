from utils.config import get_env

# 메인 테스트 계정 (A)
ID = get_env("TEST_USER_ID")
PWD = get_env("TEST_USER_PWD")

# 권한 검증용 보조 계정 (B)
ID_TEMP = get_env("TEST_USER_ID_SUB")
PWD_TEMP = get_env("TEST_USER_PWD_SUB")