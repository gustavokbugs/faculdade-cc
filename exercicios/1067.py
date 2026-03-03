def is_odd(n):
    return n % 2 != 0


def main():
    n = int(input("Digite um número inteiro: "))
    for i in range(1, n + 1):
        if is_odd(i):
            print(i)


if __name__ == "__main__":
    main()
