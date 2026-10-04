#!/bin/bash

echo "🚀 [1/3] Web E2E 테스트를 시작합니다..."
pytest tests/web/ --alluredir=allure-results --clean-alluredir

echo "🚀 [2/3] Android E2E 테스트를 시작합니다..."
PLATFORM=android pytest tests/mobile/ --alluredir=allure-results

echo "🚀 [3/3] iOS E2E 테스트를 시작합니다..."
PLATFORM=ios pytest tests/mobile/ --alluredir=allure-results

echo "✨ 모든 테스트가 완료되었습니다! Allure 리포트를 띄웁니다..."
/opt/homebrew/bin/allure serve allure-results
