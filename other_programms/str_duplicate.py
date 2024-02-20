def remove_duplicate(input_str):
    remove_char = set(input_str)
    result_str = ''.join(remove_char)
    return result_str

print(remove_duplicate("AnkurSingh".lower()))