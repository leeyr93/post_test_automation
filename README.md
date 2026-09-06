# Post Test Automation

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-E2E_Testing-2EAD33?logo=playwright&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-Testing_Framework-0A9EDC?logo=pytest&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Report-F2B300?logo=allure&logoColor=white)

> 웹 게시판 서비스의 **E2E 테스트 자동화 프로젝트**입니다.
> QA 테스트 케이스 명세서를 기반으로 **56개의 독립된 시나리오(1:1 매핑)**를 구현했으며, Allure Report를 연동하여 시각적인 테스트 결과를 제공합니다.

---

## 테스트 자동화 대시보드
이 프로젝트는 GitHub Pages를 통해 실시간 테스트 결과 대시보드를 제공합니다.
👉 **[테스트 자동화 Allure 대시보드 보기](https://leeyr93.github.io/post_test_automation/docs/)**

---

## 기술 스택
- **언어:** Python 3.12
- **프레임워크:** pytest
- **자동화 도구:** Playwright
- **디자인 패턴:** Page Object Model (POM)
- **리포팅:** Allure Report

---

## 테스트 커버리지 요약 (총 56개 시나리오)
기존의 다중 검증 로직을 단일 책임 원칙에 따라 분리하여, 기능별로 독립된 테스트 환경을 구축했습니다.
*(※ 전체 56개 상세 시나리오의 통과 여부 및 실행 기록은 상단의 **Allure 대시보드 링크**에서 확인하실 수 있습니다.)*

| 도메인 | 주요 검증 내용 | 시나리오 수 |
|---|---|---|
| **로그인 / 로그아웃** | UI 요소 검증, 상태별 버튼 노출, 실패 케이스 제어 | 5개 |
| **회원가입** | 유효성(Validation) 실패 케이스 6종, 가입 성공 흐름 | 3개 |
| **계정 찾기 (ID/PW)** | 사용자 정보 매칭 실패 예외 처리, 성공 시 리다이렉트 흐름 | 16개 |
| **비밀번호 재설정** | 보안성 제어, 비밀번호 변경 후 새로운 E2E 로그인 플로우 | 4개 |
| **게시글 (CRUD)** | 작성/수정/삭제 권한 제어(본인 vs 타인), 키워드 검색 로직 | 7개 |
| **댓글 (CRUD)** | 댓글 작성, 본인/타인 게시글 및 댓글 간의 복합적인 권한 제어 로직 | 9개 |
| **파라미터화 테스트** | `pytest.mark.parametrize`를 활용한 반복 데이터(Data-Driven) 검증 | 12개 |

---

## 주요 프로젝트 구조
```text
post_test_automation/
├── tests/
├── services/
├── pages/
├── test_data/
├── conftest.py
└── docs/
```

---

## 로컬 실행 방법

**1. 환경 셋업**
```bash
# Allure CLI 설치 (Mac 기준)
brew install allure

# 의존성 패키지 설치
pip install allure-pytest playwright
playwright install
```

**2. 테스트 실행 및 리포트 조회**
```bash
# 이전 기록을 비우고 테스트 실행 (결과물 수집)
pytest --alluredir=allure-results --clean-alluredir

# 로컬 브라우저에 대시보드 띄우기
allure serve allure-results
```
*(※ 정적 리포트 업데이트: `allure generate allure-results --clean -o docs` 실행 후 깃허브 푸시)*

---

## 향후 개선 로드맵

| 단계 | 목표 | 상세 내용 |
|---|---|---|
| **Phase 1** | 테스트 신뢰성 강화 | 로케이터 스코프 및 대기(Wait) 전략 고도화, teardown 정합성 보장 |
| **Phase 2** | 구조 리팩토링 | 셀렉터 POM 이관 및 계층 경계 복원 |
| **Phase 3** | 실행 환경 및 리포팅 고도화 | 환경 설정 분리, 테스트 마커 적용, 실패 시 스크린샷 및 Trace 수집 |
| **Phase 4** | 커버리지 확장 및 CI/CD | 접근 권한, 경계값, XSS 등 엣지 케이스 추가 및 GitHub Actions 연동 |
