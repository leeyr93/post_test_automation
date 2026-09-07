# 📋 Web Board Service QA Test Automation

> 커뮤니티 웹 서비스의 **UI E2E(Playwright)** 및 **API 인터페이스(Postman/Newman)** 통합 테스트 자동화 프로젝트입니다.  
> 설계된 **QA 테스트 케이스(74개 시나리오)**와 백엔드 핵심 API(32개 엔드포인트)를 1:1로 검증하여 배포 품질을 보장합니다.

---

## 📌 주요 산출물 바로가기

| 산출물 | 설명 | 링크 |
|---|---|:---:|
| 📮 **Postman API 명세서** | 32개 API 엔드포인트 및 인가(403) 검증 명세 | [👉 Postman Documenter](https://documenter.getpostman.com/view/2584527/2sBYAxNoaj) |
| 📊 **Allure 대시보드** | 74개 UI E2E 시나리오 실행 결과 리포트 | [👉 Allure Live Report](https://leeyr93.github.io/post_test_automation/docs/) |
| 📑 **QA 테스트 케이스** | 74개 시나리오별 조건/절차/기대결과 명세서 | [👉 `qa_test_cases.csv`](./qa_test_cases.csv) |
| 🖥️ **대상 웹 서비스** | Node.js / Express 기반 웹 게시판 어플리케이션 | [👉 `leeyr93/post`](https://github.com/leeyr93/post) |

---

## 🛠️ 기술 스택

* **UI E2E Automation**: Python 3.12, `pytest`, `Playwright`, Page Object Model (POM)
* **API Test Automation**: Postman, `Newman CLI` (JavaScript Sandbox)
* **Reporting & CI**: Allure Framework, `newman-reporter-htmlextra`, GitHub Pages

---

## 📊 테스트 커버리지 요약

### 1. UI E2E 테스트 (Playwright, 총 74개 시나리오)
* **회원가입 (21개)**: 입력 유효성 21종 검증, 특수문자 차단, 중복 가입 방지
* **인증 및 세션 (11개)**: 계정 미존재/패스워드 불일치 예외 처리, 세션 쿠키 발급 및 로그아웃
* **계정 찾기 (21개)**: 아이디 마스킹 노출, 정보 불일치 차단, 비밀번호 암호화 재설정
* **게시판 & 댓글 CRUD (21개)**: 게시글/댓글 라이프사이클 및 타인 글/댓글 수정·삭제 인가 차단

### 2. 백엔드 API 테스트 (Postman, 총 32개 인터페이스)
* **Status Codes 검증**: `200 OK`, `400 Bad Request`, `403 Forbidden`, `404 Not Found`, `409 Conflict`
* **동적 데이터 연계**: 고유 계정 생성 및 최신 `post_num`, `comm_num` 정규식 파싱 체이닝
* **독립 실행(멱등성)**: 폴더 단독 실행 시에도 사전 스크립트를 통한 500/404 결여 방지

---

## 🚀 빠른 실행 가이드 (Quick Start)

### 1. API 테스트 실행 (Newman CLI)
```bash
# 콘솔에서 즉시 전체 테스트 실행 (32개 검증)
npx newman run postman_collection.json

# 대시보드 형태의 HTML 리포트 생성
newman run postman_collection.json -r htmlextra --reporter-htmlextra-export ./newman_report.html
```

### 2. UI E2E 테스트 실행 (Playwright)
```bash
# 가상환경 구성 및 패키지 설치
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install

# 전체 E2E 테스트 실행 및 Allure 결과 수집
pytest tests/ --alluredir=allure-results --clean-alluredir

# Allure 대시보드 로컬 실행
allure serve allure-results
```

---

## 📁 디렉터리 구조

```text
post_test_automation/
├── postman_collection.json # Postman API 자동화 컬렉션 (32개 엔드포인트)
├── newman_report.html      # Newman HTML 대시보드 리포트
├── qa_test_cases.csv       # QA 테스트 케이스 명세서 (74개 시나리오)
├── NOTION_PORTFOLIO.md     # 노션 포트폴리오용 원본 마크다운 템플릿
├── pages/                  # POM (Page Object Model) 페이지 액션 정의
├── tests/                  # Allure 메타데이터 기반 pytest E2E 스크립트
├── services/               # 공통 비즈니스 플로우 헬퍼 (로그인, 가입 등)
└── docs/                   # GitHub Pages 배포용 Allure 정적 리포트
```
