


def recursive_Countdown(n:int) -> None:
    if n < 0:
        print("errore!")
    elif n == 0:
        print(n)
    else:
        print(n)
        recursive_Countdown(n-1)


recursive_Countdown(5)