from email_validator import validate_email, EmailNotValidError
import dns.resolver
from .disposable_domains import load_disposable_domains

disposable_domains = load_disposable_domains()

def check_syntax(email: str):
    """Return True if syntax is valid, else False."""
    try:
        v = validate_email(email)
        return True, v.email
    except EmailNotValidError:
        return False, None

def check_disposable(email: str):
    """Return True if email is disposable."""
    domain = email.split("@")[1].lower()
    return domain in disposable_domains

def check_mx(domain: str):
    """Return True if MX record exists."""
    try:
        records = dns.resolver.resolve(domain, 'MX')
        return len(records) > 0
    except Exception:
        return False

def check_role(email: str):
    """Return True if role-based email."""
    role_prefixes = ["admin", "support", "info", "contact", "sales"]
    local_part = email.split("@")[0].lower()
    return local_part in role_prefixes
