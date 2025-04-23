def get_required_fields(json_obj):
    required_fields = []

    def recurse(obj, path=''):
        if isinstance(obj, dict):
            for k, v in obj.items():
                full_path = f"{path}.{k}" if path else k
                if v is None:
                    required_fields.append(full_path)
                else:
                    recurse(v, full_path)
        elif isinstance(obj, list) and not obj:
            required_fields.append(path)

    recurse(json_obj)
    return required_fields
