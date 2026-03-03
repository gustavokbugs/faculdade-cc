def entrevistados():
    contadorAndroid = 0
    contadorIOS = 0
    acumuladorIdade = 0

    numeroEntrevistados = int(input("Digite o numero de entrevistados: "))

    for _ in range(numeroEntrevistados):
        idade = int(input("Digite sua idade: "))
        so = input("Digite o sistema operacional [iOS / Android]: ")
        acumuladorIdade += idade

        if so == "iOS":
            contadorIOS += 1
        else:
            contadorAndroid += 1

    mediaIdade = acumuladorIdade / numeroEntrevistados
    print(
        "\nNumero de usuarios iOS: {}, numero de usuarios Android: {}. Media da idade dos entrevistados: {} ".format(
            contadorIOS, contadorAndroid, mediaIdade
        )
    )


entrevistados()
