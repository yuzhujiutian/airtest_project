python3 tools/clear_history.py

python3 tools/copy_history.py

python3 -m pytest --alluredir allure-results

allure generate allure-results -c -o allure-report

allure open allure-report