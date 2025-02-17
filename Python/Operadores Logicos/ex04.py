
CUSTO_PASSAGEM = 30.0
PORCENTAGEM_PAGANTES_NORMAIS = 0.38
PORCENTAGEM_ESTUDANTES = 0.62

def calcular_passageiros(acumulado):
    
    total_passageiros = acumulado / (CUSTO_PASSAGEM * (PORCENTAGEM_PAGANTES_NORMAIS + PORCENTAGEM_ESTUDANTES * 0.5))
    
    pagantes_normais = total_passageiros * PORCENTAGEM_PAGANTES_NORMAIS
    estudantes = total_passageiros * PORCENTAGEM_ESTUDANTES
    
    return int(pagantes_normais), int(estudantes)

acumulado_dia = float(input("Qual o acumulado do dia? "))
pagantes, estudantes = calcular_passageiros(acumulado_dia)

print(f"Foram {pagantes} pagantes normais.")
print(f"Foram {estudantes} estudantes.")
