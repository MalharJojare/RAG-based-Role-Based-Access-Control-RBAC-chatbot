ROLES = {
    "employee": ["general"],
    "finance": ["general", "finance"],
    "marketing": ["general", "marketing"],
    "hr": ["general", "hr"],
    "engineering": ["general", "engineering"],
    "executive": ["general", "finance", "marketing", "hr", "engineering"]
}

def is_authorized(role: str, doc_type: str) -> bool:
    return doc_type in ROLES.get(role, [])
