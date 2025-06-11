USER_ROLE_MAP = {
    "alice": "finance",
    "bob": "marketing",
    "carol": "hr",
    "dan": "engineering",
    "eve": "executive",
    "erin": "employee"
}

def get_user_role(username: str) -> str:
    return USER_ROLE_MAP.get(username.lower(), "employee")
