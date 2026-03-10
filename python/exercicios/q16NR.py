def somar_valores_positivos(vetor, tamanho):
    soma = 0
    for i in range(tamanho):
        if vetor[i] > 0:
            soma = soma + vetor[i]
    return soma


def obter_vetor():
    return [2, -4, 7, 0, -1, 4]


def exibir_resultado(resultado):
    print(f"Soma dos valores positivos: {resultado}")


def main():
    vetor = obter_vetor()
    tamanho = len(vetor)
    resultado = somar_valores_positivos(vetor, tamanho)
    exibir_resultado(resultado)


if __name__ == "__main__":
    main()
