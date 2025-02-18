A = input("Informe um valor para variável A: ")
B = input("Informe um valor para variável B: ")

if A>B:
    aux=A
    A=B
    B=aux
    print("O valor da variável A agora é: ", A)
    print("O valor da variável B agora é: ", B)
else:
    print("A variável A continua com o valor: ", A)
    print("A variável B continua com o valor: ", B)