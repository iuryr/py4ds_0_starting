from os import get_terminal_size

def ft_tqdm(lst: range) -> None:
    COLS = get_terminal_size()[0]
    total = len(lst)
    for i in range(1, total + 1):
        completion_pct = round((i/total) * 100)
        print(f"\r{completion_pct:3}%|", end="")
        yield 

