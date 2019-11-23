Commands to test - 

pytest .
pytest -k add_remove_elements
pytest -m "not error"
pytest -m high_priority
pytest -m sanity_tests
pytest -m selenium_error
pytest -m assert_error
pytest -m python_error

pytest -n 5 --browser "chrome" --executor "remote"
pytest -n 5 --browser "firefox"

docker run --network="host" --rm -it -v ~/shared_folder/pytest_framework:/src -v AllureReports:/AllureReports -e ENABLE_PYTEST_CACHE=False -e ENABLE_ALLURE_REPORT=True -e ENABLE_MULTITHEAD=True -e THREAD_COUNT=5 benjose22/selenium_pytest_remote:v1.2 --browser "chrome" --executor "remote"

======================

Need to add screenshots on faliure
Need to add numpy/pandas for data
Need to add db related tests
Need to solve autoit related on headless 

