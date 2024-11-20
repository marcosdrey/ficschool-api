def is_name_valid(name: str):
    list_names = name.split(' ')
    return all(n.isalpha() for n in list_names) and len(name) > 3
