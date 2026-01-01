# EmailCheck Pro API

A free email validation API built with FastAPI.

## Features
- Syntax validation
- MX record check
- Disposable email detection
- Role-based email detection

## Endpoint
`GET /validate?email=<email_address>`

**Response Example:**

```json
{
  "email": "test@example.com",
  "valid_syntax": true,
  "disposable": false,
  "mx_found": true,
  "role_based": false
}
