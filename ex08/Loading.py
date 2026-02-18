from os import get_terminal_size

def ft_tqdm(lst: range) -> None:
    """
    Adds side effect of progress bar to stdout each time the range object
    passed as input has a value requested.
    """
    COLS = get_terminal_size()[0]
    pct_display_size = 6 # "100%|["
    total_iterations = len(lst)
    total_it_digits = len(str(total_iterations))
    iter_display_size = 2 * total_it_digits + 2 #]number/number
    #1 below is '>' char
    bar_size = COLS - 1 - pct_display_size - iter_display_size

    for i in range(1, total_iterations + 1):
        completion_pct = round((i/total_iterations) * 100)
        filled = round((completion_pct/100) * bar_size)

        pct_display = f"\r\x1b[2K{completion_pct:3}%|["
        bar = "=" * filled + ">" + " " * (bar_size - filled)
        iter_display = f"]{i:3}/{total_iterations}"

        print(pct_display, bar, iter_display,sep="", end="", flush=True)
        yield 

