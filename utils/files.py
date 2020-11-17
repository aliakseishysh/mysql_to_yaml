def save_to_yaml(filename, yaml_dump):
    try:
        with open(filename, 'w') as f:
            f.write(yaml_dump)
            return f"save_to_yaml {filename}: OK"
    except:
        return f"save_to_yaml {filename}: Fail"