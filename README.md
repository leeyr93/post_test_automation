# Web / App 게시판 서비스 E2E & API 테스트 자동화

> Web(Playwright) 및 App(Appium) 환경의 **게시판 서비스 테스트 자동화** 프로젝트입니다.

---

## 주요 산출물

| 산출물 | 설명 | 링크 |
|---|---|:---:|
| **대상 서비스** | Node.js 백엔드 및 Flutter 모바일 앱 | [`leeyr93/post`](https://github.com/leeyr93/post) |
| **QA 테스트 케이스** | E2E 시나리오 조건·절차·기대결과 명세 | [`docs/qa_test_cases.csv`](./docs/qa_test_cases.csv) |
| **API 테스트 명세서** | 전체 API 및 예외/보안 검증 명세 | [Postman Documenter](https://documenter.getpostman.com/view/2584527/2sBYAxPUrH) |
| **Allure 대시보드** | Web / App 통합 E2E 실행 결과 리포트 | [Allure Live Report](https://leeyr93.github.io/post_test_automation/docs/) |
| **Newman 리포트** | API 자동화 실행 결과 HTML 리포트 | [Newman Live Report](https://leeyr93.github.io/post_test_automation/docs/newman_report.html) |

---

## 기술 스택

- **Web E2E**: Python 3.12, Playwright, pytest
- **App E2E**: Appium (Flutter - Android / iOS)
- **API Test**: Postman, Newman
- **Reporting**: Allure Framework, GitHub Pages

---

## 테스트 범위 및 주요 검증 전략

### 1. E2E 테스트 (Playwright / Appium)
- **POM(Page Object Model) 패턴**: 화면 UI 요소와 테스트 로직을 분리해 유지보수성 향상
- **회원 인증 및 세션**: 유효성 검증, 중복 방지, 세션 유지 및 비밀번호 재설정 플로우 검증
- **게시판 & 댓글 CRUD**: 작성부터 조회·수정·삭제 라이프사이클 및 타인 글·댓글 제어 시 비인가 접근 차단
- **크로스 플랫폼 검증**: Web 브라우저 및 Mobile(iOS / Android) 환경의 핵심 시나리오 100% 검증

### 2. API 테스트 (Postman / Newman)
- **정상 및 예외 방어 로직 검증**: 정상 처리(`200`) 및 입력 오류(`400`), 미가입(`404`), 중복(`409`) 상태 코드 검증
- **비인가 접근 차단 검증**: 타인 게시글·댓글 수정·삭제 시도에 대한 서버의 차단(`403`) 로직 자동 검증
- **동적 데이터 연동**: API 응답값(게시글/댓글 번호)을 추출해 다음 테스트에 자동 전달되도록 구성
- **안정적인 반복 실행**: 사전 스크립트로 임시 데이터를 자동 생성하여 테스트 간 독립성 확보

---

## 실행 가이드

### 1. 환경 설정
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

### 2. 테스트 실행
```bash
# Web & App(Android/iOS) E2E 테스트 실행 및 Allure 대시보드 자동 실행
bash run_all_tests.sh

# API 테스트 실행 및 Newman HTML 리포트 생성
npx newman run docs/postman_collection.json -r cli,htmlextra --reporter-htmlextra-export ./docs/newman_report.html
```
