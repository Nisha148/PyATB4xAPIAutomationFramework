Python API Automation Framework

Tech Stack
- Python 3.12
- Requests - HTTP Requests
- PyTest- Testing Framework
- Reporting - Allure report, Pytest, HTML
- Test Data - CSV, Excel, JSON, Faker
- Advance API Testcase - jsonschema
- Parallel Execution - x distribute (xdist)


how to install Packages

```pip install requests pytest pytest-html faker allure-pytest jsonschema```


how to run test case parallel

```pip install pytest-xdist```

How to run the Basic Test with Allure report

```pytest tests/tests/crud/test_create_booking.py```