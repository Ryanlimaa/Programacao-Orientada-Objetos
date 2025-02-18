def verificar_doacao():
    idade = int(input("Qual sua idade? "))
    if idade < 19 or idade > 69:
        print("Infelizmente, você não pode ser doador.")
        return

    peso = float(input("Qual seu peso? "))
    if peso < 50:
        print("Infelizmente, você não pode ser doador.")
        return

    tatuagem = input("Você fez alguma tatuagem no último ano (VERDADEIRO ou FALSO)? ").strip().upper()
    if tatuagem == "VERDADEIRO":
        print("Infelizmente, você não pode ser doador.")
        return

    alcool = input("Você ingeriu álcool nas últimas 12 horas (VERDADEIRO ou FALSO)? ").strip().upper()
    if alcool == "VERDADEIRO":
        print("Infelizmente, você não pode ser doador.")
        return

    print("Parabéns, você pode doar sangue.")

    verificar_doacao()
def verificar_doacao():
    idade = int(input("Qual sua idade? "))
    if idade < 19 or idade > 69:
        print("Infelizmente, você não pode ser doador.")
        return

    peso = float(input("Qual seu peso? "))
    if peso < 50:
        print("Infelizmente, você não pode ser doador.")
        return

    tatuagem = input("Você fez alguma tatuagem no último ano (VERDADEIRO ou FALSO)? ").strip().upper()
    if tatuagem == "VERDADEIRO":
        print("Infelizmente, você não pode ser doador.")
        return

    alcool = input("Você ingeriu álcool nas últimas 12 horas (VERDADEIRO ou FALSO)? ").strip().upper()
    if alcool == "VERDADEIRO":
        print("Infelizmente, você não pode ser doador.")
        return

    print("Parabéns, você pode doar sangue.")

verificar_doacao()
