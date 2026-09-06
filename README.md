# 📋 Web Board Service E2E Test Automation

> 웹 게시판 서비스의 **E2E(End-to-End) 테스트 자동화 프로젝트**입니다.  
> 설계된 **QA 테스트 케이스 명세서(76개 시나리오)를 기반으로 자동화 코드를 1:1로 구현**했으며, Allure Framework를 연동하여 시각적인 테스트 결과 대시보드를 제공합니다.

---

## 📌 산출물 바로가기

| 산출물 | 설명 | 링크 |
|---|---|---|
| 📊 **Allure 대시보드** | 76개 전체 시나리오 실행 결과 및 상세 리포트 | [👉 실시간 대시보드 열기](https://leeyr93.github.io/post_test_automation/docs/) |
| 📑 **QA 테스트 케이스 명세서** | 76개 시나리오별 Precondition, Step, Expected Result 정의 문서 | [👉 `qa_test_cases.csv` 보기](./qa_test_cases.csv) |
| 📮 **Postman API 명세서** | 백엔드 REST API 인터페이스 및 권한 검증 명세 (Web View) | [👉 웹 API 문서 보기 (링크 생성 후 교체 예정)](#) |
| 🖥️ **대상 웹 서비스 저장소** | Node.js / Express 기반 웹 게시판 어플리케이션 | [👉 `leeyr93/post` 저장소](https://github.com/leeyr93/post) |

---

## 🛠️ 기술 스택

- **언어:** Python 3.12
- **테스트 프레임워크:** pytest
- **E2E 자동화 도구:** Playwright
- **디자인 패턴:** Page Object Model (POM)
- **리포팅:** Allure Report

---

## 📊 테스트 커버리지 (총 76개 시나리오)

QA 테스트 케이스 명세서와 1:1로 매핑된 시나리오 구성입니다.

| 도메인 | 주요 검증 내용 | 시나리오 수 |
|---|---|:---:|
| **회원가입** | UI 요소 검증, 21종 입력 유효성 검증(길이, 영문/숫자 혼합, 특수문자 차단, 이메일 포맷 등), 중복 가입 방지 및 가입 성공 흐름 | **23개** |
| **로그인 / 로그아웃** | UI 검증, 계정 미존재/비밀번호 불일치 예외 처리, 세션 상태별 버튼 노출, 로그인/로그아웃 및 화면 이동 | **11개** |
| **아이디 찾기** | UI 검증, 이름/이메일 미입력 및 불일치 예외 처리, 일치 정보 입력 시 아이디 마스킹 노출 및 링크 이동 | **11개** |
| **비밀번호 찾기** | UI 검증, 계정 불일치 예외 처리, 정상 확인 시 비밀번호 재설정 페이지 이동 | **10개** |
| **비밀번호 재설정** | UI 검증, 새 비밀번호 불일치 예외 처리, 재설정 성공 후 신규 비밀번호 로그인 검증 | **4개** |
| **게시글 (CRUD)** | 신규 게시글 등록 및 목록 반영, 키워드 검색(결과 유/무), 페이징 전환, 본인/타인 글 수정 및 삭제 권한 제어 | **8개** |
| **댓글 (CRUD)** | 댓글 등록, 본인/타인 게시글 및 본인/타인 댓글 조합에 따른 수정/삭제 버튼 노출 권한 검증 | **9개** |
| **합계** | **비즈니스 전 과정 1:1 매핑 자동화** | **총 76개** |

---


---

## 📡 대상 서비스 API 명세 요약 (Tested Interfaces)

본 E2E 자동화 테스트가 검증하는 주요 백엔드(Node.js) API 엔드포인트입니다.
*(※ 전체 요청/응답 데이터 구조 및 상태 코드(400, 403, 409 등)에 대한 상세 명세는 상단의 **Postman API 명세서 링크**에서 확인 가능합니다.)*

| Domain | Method | Endpoint | Description | Auth / 권한 검증 |
|---|:---:|---|---|---|
| **Auth** | `POST` | `/join` | 신규 사용자 회원가입 | 아이디 정규식 검사, 중복 검사 (409) |
| **Auth** | `POST` | `/login` | 사용자 세션 로그인 | 계정 존재 여부 및 패스워드 일치 확인 |
| **Auth** | `GET` | `/logout` | 현재 세션 만료 및 로그아웃 | - |
| **Board** | `GET` | `/board_list` | 게시글 페이징 조회 및 검색 | `?page=N&boardSearch=Keyword` |
| **Board** | `POST` | `/board_write` | 신규 게시글 등록 | 로그인 세션 필요 |
| **Board** | `POST` | `/board_delete` | 특정 게시글 삭제 | 로그인 세션 및 **본인 작성 글 검증 (403)** |
| **Comment**| `POST` | `/comm_write` | 특정 게시글에 댓글 등록 | 로그인 세션 필요 |
| **Comment**| `POST` | `/comm_update` | 작성한 댓글 내용 수정 | 로그인 세션 및 **본인 댓글 검증 (403)** |
| **Comment**| `POST` | `/comm_delete` | 작성한 댓글 삭제 | 로그인 세션 및 **본인 댓글 검증 (403)** |

## 📁 디렉터리 구조

```text
post_test_automation/
├── pages/                  # Page Object Model: 페이지별 UI Locator 및 인터랙션 액션
├── services/               # 공통 비즈니스 플로우 헬퍼 (로그인/가입/글작성 등)
├── test_data/              # Data-Driven 유효성 검증 데이터셋
├── tests/                  # Allure 메타데이터가 적용된 실제 테스트 스크립트
├── docs/                   # GitHub Pages 배포용 Allure 정적 리포트
├── qa_test_cases.csv       # QA 테스트 케이스 명세서
├── conftest.py             # pytest Fixture 정의 (Browser Context, 세션 관리 등)
└── pytest.ini              # pytest 실행 설정
```

---

## 🚀 실행 방법

### 1. 환경 설정 및 패키지 설치
```bash
# 가상환경 구성
python3 -m venv venv
source venv/bin/activate

# 의존성 패키지 설치
pip install -r requirements.txt  # 또는: pip install allure-pytest playwright pytest
playwright install
```

### 2. 테스트 실행 및 리포트 확인
```bash
# 전체 테스트 실행 (이전 결과 초기화 및 allure-results 수집)
pytest tests/ --alluredir=allure-results --clean-alluredir

# 로컬에서 Allure 대시보드 즉시 확인 (택 1)
npx allure-commandline serve allure-results   # npx 사용 시
allure serve allure-results                  # Allure CLI 설치 시
```

### 3. GitHub Pages 정적 리포트(`docs/`) 빌드
```bash
npx allure-commandline generate allure-results --clean -o docs
git add docs/
git commit -m "docs: update allure report"
git push origin main
```
---

## 🚀 향후 개선 로드맵 (Future Work)

대규모 실무 환경 확장을 위해 고려 중인 고도화 방향성입니다.

| 단계 | 목표 | 개선 상세 |
|---|---|---|
| **Phase 1** | **테스트 실행 속도 최적화** | UI 기반의 Setup(글 생성 등) 로직을 백엔드 REST API 호출로 대체하여 오버헤드 최소화 |
| **Phase 2** | **테스트 완벽 격리 및 병렬 처리** | 고정 계정(`.env`) 의존성을 제거하고 `pytest-xdist`를 도입하여 다중 스레드 병렬 실행(Parallel Test) 가능 구조 확립 |
| **Phase 3** | **CI/CD 무인 자동화 구축** | GitHub Actions 연동으로 PR 및 Push 이벤트 시 자동 테스트 수행 및 Allure 대시보드 무인 배포 |
| **Phase 4** | **시각적 디버깅 도구 고도화** | 테스트 실패 시 스크린샷 캡처 및 Playwright Trace 뷰어 기록을 Allure 리포트에 자동 첨부하여 추적성(Traceability) 강화 |
