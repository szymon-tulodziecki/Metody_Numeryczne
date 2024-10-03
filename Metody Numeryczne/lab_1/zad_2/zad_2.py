import numpy as np

xp = 0
xk = 2 * np.pi

krok = 0.1

liczba_punktow = np.abs(xk - xp) / krok
liczba_punktow_int = int(np.ceil(liczba_punktow))

x = xp

print(f"liczba punktow x: {liczba_punktow_int}")

for i in range(0, liczba_punktow_int):
    x += krok
    print("%d. sin(%f) = %f, cos(%f) = %f, tan(%f) = %f, ctg(%f) = %f " % (i, x, np.sin(x), x, np.cos(x), x, np.tan(x), x, (1.0 / np.tan(x))))