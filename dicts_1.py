def update_dictionary(d, key, value):
    # If we have such key, we add value to this key
    if key in d:
        d[key].append(value)
    # If there's no such key but there's 'key * 2', we add value to 'key * 2'
    # For example: There's no key 3, but there's key 6, so we add value to 6
    elif key not in d and (key * 2) in d:
        d[key * 2].append(value)
    # If there's no key and key * 2, we create key * 2 and set 'value' to it
    elif key not in d and (key * 2) not in d:
        d[key * 2] = [value]
    return d


d = {}
# Check 'update_dictionary' function with empty dictionary, key = 0, value = -5
update_dictionary(d, 0, -5)
# It will output {0: [-5]} No key 0, so 0 * 2 = 0
print(d)
update_dictionary(d, 1, -1)
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 3, -3)
print(d)