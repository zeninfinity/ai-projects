import re

def get_required_fields(ts_content):
    interface_match = re.search(r'interface\s+\w+\s*{([^}]*)}', ts_content, re.DOTALL)
    if not interface_match:
        return []

    body = interface_match.group(1)
    lines = body.split('\n')
    required_fields = []

    for line in lines:
        line = line.strip()
        if not line or ':' not in line or '?' in line:
            continue
        field = line.split(':')[0].strip()
        required_fields.append(field)

    return required_fields
