# 게시판 서비스 E2E & API 테스트 자동화

> 웹 게시판 서비스의 **E2E(Playwright)** 및 **API 인터페이스(Postman)** 통합 테스트 자동화 프로젝트입니다.

---

## 주요 산출물 바로가기

| 산출물 | 설명 | 링크 |
|---|---|:---:|
| **대상 웹 서비스** | Node.js / Express 기반 웹 게시판 서비스 | [`leeyr93/post`](https://github.com/leeyr93/post) |
| **QA 테스트 케이스** | E2E 시나리오 조건·절차·기대결과 명세 | [`docs/qa_test_cases.csv`](./docs/qa_test_cases.csv) |
| **Postman API 명세서** | 전체 API 및 예외/보안 검증 명세 | [Postman Documenter](https://documenter.getpostman.com/view/2584527/2sBYAxNoaj) |
| **Allure 대시보드** | E2E 자동화 실행 결과 리포트 | [Allure Live Report](https://leeyr93.github.io/post_test_automation/docs/) |
| **Newman 리포트** | API 자동화 실행 결과 HTML 리포트 | [Newman Live Report](https://leeyr93.github.io/post_test_automation/docs/newman_report.html) |

---

## 기술 스택

* **E2E Automation**: Python 3.12, Playwright, pytest, POM (Page Object Model), Allure Framework, GitHub Pages
* **API Test Automation**: Postman, Newman CLI, JavaScript Sandbox, newman-reporter-htmlextra, GitHub Pages

---

## 테스트 범위 및 주요 검증 전략

### 1. E2E 테스트 (Playwright, 총 74개 시나리오)
* **회원가입 (21개)**: 입력 유효성 21종 검증, 특수문자 차단, 중복 가입 방지
* **인증 및 세션 (11개)**: 계정 미존재/패스워드 불일치 예외 처리, 세션 쿠키 발급 및 로그아웃
* **계정 찾기 (21개)**: 아이디 마스킹 노출, 정보 불일치 차단, 비밀번호 암호화 재설정
* **게시판 & 댓글 CRUD (21개)**: 게시글/댓글 라이프사이클 및 타인 글/댓글 수정·삭제 비인가 접근 차단

### 2. API 테스트 (Postman, 총 32개 API)
* **Status Codes 검증**: `200 OK`, `400 Bad Request`, `403 Forbidden`, `404 Not Found`, `409 Conflict`
* **동적 데이터 연계**: 고유 계정 생성 및 최신 `post_num`, `comm_num` 정규식 파싱 체이닝
* **안정적인 반복 실행**: 폴더 단독 실행 시에도 사전 스크립트로 필수 데이터를 생성해 404/500 에러 방지

---

## 실행 가이드

### 1. E2E 테스트 실행 (Playwright)
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

### 2. Allure 정적 리포트 재생성 (GitHub Pages 배포용)
```bash
allure generate allure-results --clean -o docs
```

### 3. API 테스트 실행 (Newman CLI)
```bash
# 리포트 생성을 위한 npm 패키지 설치
npm install newman-reporter-htmlextra

# 콘솔에서 즉시 전체 테스트 실행 (32개 검증)
npx newman run docs/postman_collection.json

# 대시보드 형태의 HTML 리포트 생성
npx newman run docs/postman_collection.json -r htmlextra --reporter-htmlextra-export ./docs/newman_report.html
```


