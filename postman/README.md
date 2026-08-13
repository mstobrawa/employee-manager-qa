# Employee Manager QA – Postman API Tests

Postman collection for testing the Employee Manager REST API.

## Requirements

- Employee Manager application running locally
- API available at:
  `http://127.0.0.1:8000`

## Collection Structure

### 01 - Authentication

- `POST /api/login`

The login endpoint returns a Bearer access token and its expiration time.

After a successful login, the token is automatically stored in the collection variable:

`auth_token`

### 02 - Employees

- `GET /api/employees`
- `POST /api/employees`
- `PUT /api/employees/{id}`
- `DELETE /api/employees/{id}`

### 03 - Reset

- `POST /api/employees/reset`

### 04 - Negative Tests

- `POST /api/employees` – invalid data (`422`)
- `DELETE /api/employees/{id}` – non-existent employee (`404`)

### Health Check

- `GET /health`

## Authentication

Protected endpoints use Bearer Token authentication:

`Bearer {{auth_token}}`

The token is automatically obtained and stored after executing:

`POST /api/login`

There is no need to manually copy the token to individual requests.

## Test Credentials

**Username:** `admin`  
**Password:** `admin`

## Automated Postman Tests

The collection includes basic assertions covering:

- HTTP status codes
- response structure
- required response fields
- employee data
- authentication response
- validation errors (`422`)
- non-existent resources (`404`)
- reset operation
- health check

## Token Expiration

The access token is valid for **600 seconds (10 minutes)**.

After the token expires, run `POST /api/login` again to obtain a new token.

The access token itself is **not stored in the repository**. Only the collection variable definition is included in the exported collection.
