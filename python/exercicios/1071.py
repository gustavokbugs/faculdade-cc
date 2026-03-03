def is_odd(num):
    return num % 2 != 0


def sum_odd_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_odd(num):
            total += num

    return total


def main():
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))

    if x > y:
        x, y = y, x

    resultado = sum_odd_numbers(x, y)
    print(f"SOMA DOS IMPARES = {resultado}")


if __name__ == "__main__":
    main()
