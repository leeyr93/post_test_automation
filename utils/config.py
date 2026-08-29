"""
환경 변수 로딩을 담당하는 단일 진입점.

utils/user.py, utils/url.py 가 이 모듈을 임포트하는 순간
load_dotenv() 가 먼저 실행되므로 .env 로딩 순서가 자동으로 보장된다.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 루트 = utils/ 의 부모 디렉터리
# 실행 위치(cwd)와 무관하게 .env 를 찾기 위해 절대 경로로 고정한다.
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


def get_env(key: str, default: str | None = None) -> str:
    """환경 변수를 읽는다. 값도 기본값도 없으면 즉시 실패시킨다."""
    value = os.getenv(key, default)
    if value is None:
        raise RuntimeError(
            f"환경 변수 '{key}' 가 설정되지 않았습니다.\n"
            f".env.example 을 복사해 .env 를 만들고 값을 채워주세요.\n"
            f"  cp .env.example .env"
        )
    return value