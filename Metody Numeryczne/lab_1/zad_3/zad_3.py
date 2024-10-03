import numpy as np

while True:
    try:
        n = int(input('Podaj liczbe n: '))
        if n <= 0:
            print("N musi byc wieksze od 0!")
        else:
            break
    except ValueError as err:
        print(err)
i = 0
x = 2
for i in range(i, n):
    print(x)
    x += 2