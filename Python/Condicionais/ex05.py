
nome_hospede = input("Digite seu nome: ")

apartamento = input("Digite o tipo do apartartamento (A, B, C ou D): ")

diarias_utilizadas = int(input("Digite o numero de diarias utilizadas pelo hospede: "))

consumo_interno = int(input("Digite o valor do consumo interno: "))

if apartamento == 'A':
    valor_diaria = 150.00
elif apartamento == 'B':
    valor_diaria = 100.00
elif apartamento == 'C':
     valor_diaria = 75.00
elif apartamento == 'D':
    valor_diaria = 50.00

total_diaria = diarias_utilizadas * valor_diaria

subtotal = total_diaria + consumo_interno

taxa_servico = subtotal * 0.10

total_geral = subtotal + taxa_servico

print(f"Nome do hóspede: {nome_hospede }")
print(f"Tipo do apartamento: {apartamento }")
print(f"Número de diárias: {diarias_utilizadas }")
print(f"Valor unitário da diária: R$ {valor_diaria:.2f}")
print(f"Valor total das diárias: R$ {total_diaria:.2f}")
print(f"Valor do consumo interno: R$ {consumo_interno:.2f}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Taxa de serviço (10%): R$ {taxa_servico:.2f}")
print(f"Total geral: R$ {total_geral:.2f}")


