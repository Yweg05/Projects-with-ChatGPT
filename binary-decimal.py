"""

A simple program that converts from decimal to binary or from binary to decimal.

By Migel

"""


def d_to_b(num):
    cociente, resto = divmod(num, 2)
    result = ""

    while cociente > 1:
        result = f"{resto}{result}"

        cociente, resto = divmod(cociente, 2)
    print(f"{cociente}{resto}{result}")


def b_to_d(num):
    num_inverso = str(num)[::-1]
    result = 0

    for index, x in enumerate(num_inverso):
        if x == "1":
            x = 2**index

        result = result + x
    print(result)


def main():
    while True:
        print(
            "\nWhat do you wanna do?\n1. Decimal to binary\n2. Binary to decimal\nAnything else. Exit"
        )
        try:
            choice = int(input("\n"))

            if choice == 1:
                d_to_b(int(input("What number do you wanna convert?  ")))

            elif choice == 2:
                num = input("What number do you wanna convert (only '1' and '0')?  ")

                if all(a in "01" for a in num):
                    b_to_d(int(num))
                else:
                    print("Only '0' and '1'")

            else:
                print("Bye!")
                break

        except ValueError:
            print("Make sure you introduce a valid number")


main()
