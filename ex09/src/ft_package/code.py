def count_in_list(lst : list[str], word : str) -> int:
    count = sum([1 for string in lst if string == word])
    return count
