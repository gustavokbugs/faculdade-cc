def validar_valor(valor, minimo=0, maximo=10):
    return minimo <= valor <= maximo


def ler_valor_validado(mensagem, minimo=0, maximo=10):
    while True:
        try:
            valor = float(input(mensagem))
            if validar_valor(valor, minimo, maximo):
                return valor
            else:
                print(f"Valor inválido! Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida! Digite um número.")


def calcular_media_ponderada(a, b, c, peso_a=2, peso_b=3, peso_c=5):
    return (a * peso_a + b * peso_b + c * peso_c) / (peso_a + peso_b + peso_c)


def exibir_media(media):
    print(f"MEDIA = {media:.1f}")


def main():
    a = ler_valor_validado("Digite o primeiro valor: ")
    b = ler_valor_validado("Digite o segundo valor: ")
    c = ler_valor_validado("Digite o terceiro valor: ")

    media = calcular_media_ponderada(a, b, c)
    exibir_media(media)


if __name__ == "__main__":
    main()
