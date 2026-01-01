from pydantic import BaseModel

class ValidationResult(BaseModel):
    email: str
    valid_syntax: bool
    disposable: bool
    mx_found: bool
    role_based: bool
