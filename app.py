# Programa de calculadora de consumo elétrico
# Autor: Thiago

# Entrada
nome_do_aparelho = input("Digite o nome do aparelho: ")
potencia_watts = float(input("Digite a potência do aparelho (em watts): "))
horas_uso = float(input("Digite o número de horas de uso por dia: "))

# Processamento
consumo_diario = (potencia_watts * horas_uso) / 1000  # Convertendo para kWh
consumo_mensal = consumo_diario * 30  # Considerando 30 dias no mês

# Saída
print(f"\nAparelho: {nome_do_aparelho}")
print(f"Consumo Diário: {consumo_diario:.2f} kWh")
print(f"Consumo Mensal: {consumo_mensal:.2f} kWh")