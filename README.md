# Employee Manager – QA Portfolio Project

A QA portfolio project covering manual testing, API testing, UI automation, test documentation, defect reporting, and test reporting for a sample Employee Manager application.

## Project Overview

The project demonstrates a complete QA workflow:

- requirements review
- test planning
- manual test case design
- test case management in TestRail
- defect reporting in Jira
- REST API testing with Postman
- API automation with Python, pytest and requests
- UI automation with Selenium
- Page Object Model
- explicit waits
- automated test reporting

The tested application provides employee management functionality including authentication, employee CRUD operations, validation, data reset, and theme switching.

## Testing Scope

### Manual Testing

Manual test cases cover:

- Name
- Salary
- Age
- Position
- On leave

The test cases were designed using:

- Equivalence Partitioning (EP)
- Boundary Value Analysis (BVA)
- Decision Table Testing

A total of **29 manual test cases** were created and executed in TestRail:

- 28 Passed
- 1 Blocked
- 0 Failed

The blocked case concerns the expected behaviour of leading and trailing spaces in the Name field and requires clarification.

### Defect Reporting

Three defects were identified and documented in Jira:

- KAN-1 – Previous validation error remains visible after entering Edit mode
- KAN-2 – Deleting an employee in edit mode blocks further application use
- KAN-3 – Previously issued authentication token remains valid after logout

### API Testing

API testing was performed with Postman.

The collection covers:

- `POST /api/login`
- `GET /api/employees`
- `POST /api/employees`
- `PUT /api/employees/{id}`
- `DELETE /api/employees/{id}`
- `POST /api/employees/reset`
- `GET /health`

Negative scenarios include:

- invalid employee data → `422`
- non-existent employee → `404`

The Postman collection automatically stores the authentication token in the `auth_token` collection variable.

The token itself is not stored in the repository.

### API Automation

API automation was implemented using:

- Python
- pytest
- requests

The automated API tests cover:

- authentication
- employee retrieval
- employee creation
- employee update
- employee deletion
- reset
- validation
- `404` responses

Current result:

**13 passed**

### UI Automation

UI automation was implemented using:

- Python
- pytest
- Selenium WebDriver
- Page Object Model
- explicit waits

The automated UI tests cover:

- login
- adding an employee
- editing an employee
- deleting an employee
- validation
- reset confirmation
- theme switching

Current result:

**7 passed**

No `time.sleep()` calls or JavaScript-based test interactions are used.

## Test Results

| Test Area           |  Tests | Result                |
| ------------------- | -----: | --------------------- |
| Manual / TestRail   |     29 | 28 Passed / 1 Blocked |
| API automation      |     13 | 13 Passed             |
| UI automation       |      7 | 7 Passed              |
| **Automated tests** | **20** | **20 Passed**         |

## Repository Structure

```text
employee-manager-qa/
├── .gitignore
├── README.md
│
├── docs/
│   ├── Employee_Manager_Test_Plan.pdf
│   ├── pytest-report.html
│   ├── selenium-report.html
│   └── screenshots/
│       ├── app-browser.png
│       └── app-terminal.png
│
├── jira/
│   └── README.md
│
├── postman/
│   ├── README.md
│   └── employee-manager-qa-api.postman_collection.json
│
├── testrail/
│   └── TESTRAIL.md
│
└── tests/
    ├── api/
    │   ├── conftest.py
    │   ├── test_auth.py
    │   ├── test_employees.py
    │   ├── test_reset.py
    │   └── test_validation.py
    │
    └── ui/
        ├── conftest.py
        ├── pages/
        │   ├── employee_page.py
        │   └── login_page.py
        ├── test_add_employee.py
        ├── test_delete_employee.py
        ├── test_edit_employee.py
        ├── test_login.py
        ├── test_reset.py
        ├── test_theme.py
        └── test_validation.py
```

## Test Documentation

### Test Plan

The complete test plan is available in:

`docs/Employee_Manager_Test_Plan.pdf`

It documents the testing approach, scope, objectives, test techniques, and planned test activities.

### TestRail

TestRail documentation and execution results are available in:

`testrail/TESTRAIL.md`

### Jira

Defect reporting documentation is available in:

`jira/README.md`

### Postman

The exported Postman collection is available in:

`postman/employee-manager-qa-api.postman_collection.json`

## Test Reports

HTML reports generated with `pytest-html` are available in the `docs/` directory:

- `pytest-report.html` – API automation report
- `selenium-report.html` – UI automation report

## Running the Tests

The Employee Manager application must be running locally before executing the API and UI tests.

The tests expect the application to be available at:

```text
http://127.0.0.1:8000
```

The tests use the Python environment configured for the project with pytest, requests and Selenium.

The API and UI suites are executed separately.

From the `tests` directory:

```bash
pytest api -v
```

Expected result:

```text
13 passed
```

Run the UI tests:

```bash
pytest ui -v
```

Expected result:

```text
7 passed
```

## Demo Authentication

The sample application uses the documented demo credentials:

```text
Username: admin
Password: admin
```

Postman authentication uses the `auth_token` collection variable for the Bearer token.

## Tools & Technologies

- Python
- pytest
- requests
- Selenium WebDriver
- Postman
- Jira
- TestRail
- Git
- pytest-html

## Project Status

**Completed**

The project includes manual QA documentation, TestRail test cases and execution results, Jira defect reports, Postman API tests, automated API tests, automated Selenium UI tests, and HTML test reports.
