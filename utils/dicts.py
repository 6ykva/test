def get_val(collection, key, default='git'):
    if key not in collection:
        return default
    if key == int():
        return 'это число'
    return collection.get(key)
