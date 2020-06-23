python3 tools/clear_log.py

pytest --alluredir allure-results

allure generate allure-results -c -o allure-report

allure open allure-report