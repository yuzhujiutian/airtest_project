python3 tools/clear_log.py

python3 -m pytest --alluredir allure-results

allure generate allure-results -c -o allure-report

allure open allure-report