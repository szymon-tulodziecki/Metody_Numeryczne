import cmath


def wprowadz_rownanie():
    while True:
        try:
            a_f = float(input("Podaj współczynnik a: "))
            b_f = float(input("Podaj współczynnik b: "))
            c_f = float(input("Podaj współczynnik c: "))
            if a_f == 0:
                print("Współczynnik a nie może być zerem dla równania kwadratowego.")
            else:
                break
        except ValueError as err:
            print(err)

    return a_f, b_f, c_f

def wyswietl_rownanie(a_f2, b_f2, c_f2):
    print("")
    print(f"Równanie: {a_f2}x^2 {b_f2:+}x {c_f2:+} ma: ")

def main():
    print("OBLICZANIE ROWNANIA KWADRATOWEGO: ax^2 + bx + c")
    a, b, c = wprowadz_rownanie()
    delta = pow(b, 2) - 4 * a * c
    sqrt_delta = cmath.sqrt(delta)

    wyswietl_rownanie(a, b, c)

    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)

    if delta == 0:
        print(f"-> Jedno rozwiązanie: x0 = {x1.real}")
    elif delta > 0:
        print(f"-> Dwa rozwiązania rzeczywiste: x1 = {x1.real} x2 = {x2.real}")
    else:
        print(f"-> Dwa rozwiązania zespolone: x1 = {x1} x2 = {x2}")

if __name__ == '__main__':
    main()