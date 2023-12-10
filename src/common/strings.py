def replace_at_index(old_string: str, substring: str, index: int) -> str:
    return old_string[:index] + substring + old_string[index + 1 :]
