n = 4
n_n = n
silnia = n

if n == 0:
    print(f"{n_n}! = 1")
else:
    while n > 1:
        silnia *=  n - 1
        n -= 1
    print(f"{n_n}! = {silnia}")
