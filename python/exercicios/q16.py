def somar_valores_positivos(vetor, tamanho):
    if tamanho == 0:
        return 0
    else:
        soma_anterior = somar_valores_positivos(vetor, tamanho - 1)
        if vetor[tamanho - 1] > 0:
            soma_anterior = soma_anterior + vetor[tamanho - 1]
        return soma_anterior


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
