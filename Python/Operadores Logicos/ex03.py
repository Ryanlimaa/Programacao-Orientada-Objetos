pedreiros = 8
horas = 72

pedreiros_disponiveis = int(input("Digite a quantidade de pedreiros disponiveis:"))

horas_necessarias = (pedreiros * horas) / pedreiros_disponiveis

print("Os " + str(pedreiros_disponiveis) + " pedreiros levarão " + str(horas_necessarias) + " horas para terminar o muro!")