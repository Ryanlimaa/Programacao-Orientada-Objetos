notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

mediafinal = (notaA + notaB) / 2

if mediafinal >= 5.0:
    print("Média %.1f - Aprovado "% mediafinal)
else:
    print("Média %.1f - Reprovado "% mediafinal)