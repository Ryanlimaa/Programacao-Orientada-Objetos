peso = int(input("Digite seu peso:"))
print(peso)

altura = float(input("Digite sua altura:"))
print(altura)

imc = peso / (altura * altura)
print("IMC = " + str(imc))

if imc < 17:
    print("Muito abaixo do peso!")

elif imc >= 17 and imc <= 18.49:
    print("Abaixo do peso!")

elif imc >= 18.50 and imc <= 24.99:
    print("Peso normal!")

elif imc >= 25 and imc <= 29.99:
    print("Acima do peso!")

elif imc >= 30 and imc <= 34.99:
    print("Obesidade 1!")

elif imc >= 35 and imc <= 39.99:
    print("Obesidade 2 (severa!)")

else:
    print("Obesidade 3 (mórbida!)")
