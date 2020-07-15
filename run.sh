source venv/bin/activate

pytest --alluredir allure-results --clean-alluredir

allure generate allure-results -c -o allure-report

allure open allure-report