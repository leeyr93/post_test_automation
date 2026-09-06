# Post Test Automation

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-E2E_Testing-2EAD33?logo=playwright&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-Testing_Framework-0A9EDC?logo=pytest&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Report-F2B300?logo=allure&logoColor=white)

> 웹 게시판 서비스의 **E2E 테스트 자동화 프로젝트**입니다.
> QA 테스트 케이스 명세서를 기반으로 **77개의 독립된 시나리오(1:1 매핑)**를 구현했으며, Allure Report를 연동하여 시각적인 테스트 결과를 제공합니다.

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

## 테스트 커버리지 요약 (총 77개 시나리오)
기존의 다중 검증 로직을 단일 책임 원칙에 따라 분리하여, 기능별로 독립된 테스트 환경을 구축했습니다.
*(※ 전체 77개 상세 시나리오의 통과 여부 및 실행 기록은 상단의 **Allure 대시보드 링크**에서 확인하실 수 있습니다.)*

| 도메인 | 주요 검증 내용 | 시나리오 수 |
|---|---|---|
| **회원가입** | UI 요소/플레이스홀더 검증, 입력 필드별 유효성 검증(22종), 중복 가입 방지 및 가입 성공 흐름 | 24개 |
| **로그인 / 로그아웃** | UI 요소 검증, 입력값 조합별 예외 처리, 상태별 버튼 노출, 로그인/로그아웃 흐름 | 11개 |
| **아이디 찾기** | UI 요소 검증, 이름/이메일 유효성 및 불일치 예외 처리, 일치 시 노출 및 링크 이동 흐름 | 11개 |
| **비밀번호 찾기** | UI 요소 검증, 일치/불일치 예외 처리, 회원가입 페이지 이동 흐름 | 10개 |
| **비밀번호 재설정** | UI 요소 검증, 비밀번호 확인 불일치 예외 처리, 재설정 성공 및 신규 비밀번호 로그인 플로우 | 4개 |
| **게시글 (CRUD)** | 작성 후 목록 반영, 키워드 검색(결과 있음/없음), 페이징 이동, 본인/타인 글 수정·삭제 권한 제어 | 8개 |
| **댓글 (CRUD)** | 댓글 작성, 본인/타인 게시글 및 댓글 간의 복합적인 권한 제어(수정/삭제 버튼 노출) 로직 | 9개 |

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
# Allure CLI 설치 (Mac 기준, 또는 npx 사용 가능)
brew install allure

# 의존성 패키지 설치
pip install -r requirements.txt  # 또는 pip install allure-pytest playwright
playwright install
```

**2. 테스트 실행 및 리포트 조회**
```bash
# 이전 기록을 비우고 테스트 실행 (결과물 수집)
pytest tests/ --alluredir=allure-results --clean-alluredir

# 로컬 브라우저에 대시보드 띄우기
allure serve allure-results
# (또는 Allure CLI 미설치 시: npx allure-commandline serve allure-results)
```
*(※ 정적 리포트 업데이트: `npx allure-commandline generate allure-results --clean -o docs` 또는 `allure generate allure-results --clean -o docs` 실행 후 깃허브 푸시)*

---

## 향후 개선 로드맵

| 단계 | 목표 | 상세 내용 |
|---|---|---|
| **Phase 1** | 테스트 신뢰성 강화 | 로케이터 스코프 및 대기(Wait) 전략 고도화, teardown 정합성 보장 |
| **Phase 2** | 구조 리팩토링 | 셀렉터 POM 이관 및 계층 경계 복원 |
| **Phase 3** | 실행 환경 및 리포팅 고도화 | 환경 설정 분리, 테스트 마커 적용, 실패 시 스크린샷 및 Trace 수집 |
| **Phase 4** | 커버리지 확장 및 CI/CD | 접근 권한, 경계값, XSS 등 엣지 케이스 추가 및 GitHub Actions 연동 |
