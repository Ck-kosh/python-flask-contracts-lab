# Lab: Contractors Lab

---

## Overview

Now it is time for you to build your own request responses!

You are working for a company that manages contracts between two parties. You need to manage sensitive data, and as such, you need to build two requests:

- One for **customer information**
- One for **contract information**

You will be using two new response codes:

- **204**: Successful response but no data to send (e.g., confirming a customer exists without sharing data).
- **404**: Not found — we cannot find the requested data.

---

## Tasks

### Task 1: Define the Problem

Build the following routes:

- `/contract/<id>`
- `/customer/<customer_name>`

---

### Task 2: Determine the Design

#### App Routes:

- `GET /contract/<id>`
  - **200**: Contract found — return contract information.
  - **404**: Contract not found.

- `GET /customer/<customer_name>`
  - **204**: Customer found — no information returned (sensitive).
  - **404**: Customer not found.

---

### Task 3: Develop the Code

- Initialize Flask
- Set up routes
- Configure responses

---

### Task 4: Test and Refine

- Debug and test during development using the provided test suite and Flask instance.

---

### Task 5: Document and Maintain

- Commit as you go with meaningful messages.
- Push commit history to GitHub periodically and when the lab is complete.

---

## Tools and Resources

- **GitHub Repo**: *Link to be provided*
- **Flask Quickstart**: [https://flask.palletsprojects.com/en/stable/quickstart/](https://flask.palletsprojects.com/en/stable/quickstart/)

---

## Instructions

### Set Up

Before coding:

1. **Fork and Clone**
   - Go to the provided GitHub repository link.
   - Fork the repository to your GitHub account.
   - Clone the forked repository to your local machine.

2. **Open and Run**
   - Open the project in VSCode.
   - Run `pipenv install` to install dependencies.
   - Run `pipenv shell` to activate the Python shell.

---

### Task 1: Define the Problem

Build the following routes:

- `/contract/<id>`
- `/customer/<customer_name>`

---

### Task 2: Determine the Design

#### App Routes:

- `/contract/<id>`
  - **200**: Contract found — return information
  - **404**: Contract not found

- `/customer/<customer_name>`
  - **204**: Customer found — return no information
  - **404**: Customer not found

---

### Task 3: Develop, Test, and Refine the Code

1. Create a **feature branch**.
2. Build the following routes:

#### `/contract/<id>`

- If the contract ID is found in the given array:
  - Return contract information with a **200** response.
- If not found:
  - Return a **404** response.

#### `/customer/<customer_name>`

- If the customer name is found:
  - Return a **204** response with an empty body.
- If not found:
  - Return a **404** response.

3. Push the feature branch and open a PR on GitHub.
4. Merge into `main`.

---

## Implementation Details

### Routes Overview

The application implements two API endpoints for managing contract and customer information:

#### `GET /contract/<id>`
- **Purpose**: Retrieves contract information by contract ID
- **Success Response (200)**:
  - Returns plain text contract information
  - Example: `GET /contract/1` returns `"This contract is for John and building a shed"`
- **Error Response (404)**:
  - Returned when the contract ID does not exist

#### `GET /customer/<customer_name>`
- **Purpose**: Verifies if a customer exists (privacy-protecting endpoint)
- **Success Response (204)**:
  - Returns with an empty body (no sensitive data exposed)
  - Example: `GET /customer/bob` returns status 204 with empty response
- **Error Response (404)**:
  - Returned when the customer name does not exist

### Sample Data

**Contracts:**
```json
[
  {"id": 1, "contract_information": "This contract is for John and building a shed"},
  {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
  {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]
```

**Customers:**
```
["bob", "bill", "john", "sarah"]
```

### Running the Application

1. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

2. Run the Flask development server:
   ```bash
   python server/app.py
   ```
   The app will be available at `http://localhost:5555`

### Testing

Run the test suite to verify all endpoints:
```bash
pipenv run pytest server/testing/app_test.py -v
```

**All 6 tests pass:**
- ✓ `/contract/<id>` route exists and returns 200 for valid contracts
- ✓ Contract information is returned correctly
- ✓ Invalid contract IDs return 404
- ✓ `/customer/<customer_name>` route exists and returns 204 for valid customers
- ✓ Customer endpoint returns empty response body
- ✓ Invalid customer names return 404

### Code Comments

The implementation includes detailed docstrings and inline comments explaining:
- Route functionality and parameters
- Response codes and their meaning
- Data lookup logic
- Privacy considerations for the customer endpoint

---

### Task 4: Document and Maintain

#### Best Practices:

- Add comments to explain logic and purpose.
- Clarify code intent for other developers.
- Include a screenshot of completed work in the README.
- Update the README to reflect functionality using [https://makeareadme.com](https://makeareadme.com).
- Delete stale branches on GitHub.
- Remove unnecessary or commented-out code.
- Update `.gitignore` if needed to exclude sensitive data
