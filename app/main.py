from fastapi import FastAPI, Query
from app.validator import check_syntax, check_disposable, check_mx, check_role
from app.schemas import ValidationResult

app = FastAPI(
    title="EmailCheck Pro API",
    description="Validate emails: syntax, MX, disposable, and role-based detection.",
    version="1.0.0"
)

@app.get("/validate", response_model=ValidationResult)
def validate_email_endpoint(email: str = Query(..., example="test@example.com")):
    # Step 1: Syntax check
    valid_syntax, normalized = check_syntax(email)
    if not valid_syntax:
        return ValidationResult(
            email=email,
            valid_syntax=False,
            disposable=False,
            mx_found=False,
            role_based=False
        )

    # Step 2: Domain checks
    domain = normalized.split("@")[1]
    mx_found = check_mx(domain)
    disposable = check_disposable(normalized)
    role_based = check_role(normalized)

    return ValidationResult(
        email=normalized,
        valid_syntax=True,
        disposable=disposable,
        mx_found=mx_found,
        role_based=role_based
    )
