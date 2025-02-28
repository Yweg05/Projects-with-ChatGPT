"""

Programa simple para facer a secuencia de Fibonacci coa lonxitude desexada.

By Migel

"""


def ask(var):
    return input(f"\nIntroduza {var}:  ")


def operate(num):
    a, b = 0, 1
    for _ in range(num):

        print(a, end=" ")

        a, b = b, a + b


def main():
    while True:
        x = int(ask("o número de sumas a realizar"))
        operate(x)

        choice = input("\nQueres repetilo (si(default)='Y')?  ").lower()
        if "" != choice != "y":
            break


main()
