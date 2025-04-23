from modules.tsrequirements import get_required_fields

with open("prompt.ts", "r") as f:
    ts_content = f.read()

required_fields = get_required_fields(ts_content)
print(required_fields)
