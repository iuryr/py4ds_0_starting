def count_in_list(lst: list[str], word: str) -> int:
    """Counts ocurrences of word in a list of words
    """
    count = sum([1 for string in lst if string == word])
    return count
