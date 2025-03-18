meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

for i in range(12):
    
    while True:
        
        try:
            temp = float(input(f"Informe a temperatura máxima de {meses[i]}: "))
            
            if temp >= -60 and temp <= 50:
                temperaturas.append(temp)
                break
            
            else:
                print("Erro: A temperatura deve estar entre -60 e 50 graus Celsius.")
        
        except ValueError:
            print("Erro: Por favor, insira um número válido. Tente novamente.")

    
media_anual = sum(temperaturas) / 12
meses_escaldantes = sum(1 for temp in temperaturas if temp > 33)
mes_mais_quente = meses[temperaturas.index(max(temperaturas))]
mes_menos_quente = meses[temperaturas.index(min(temperaturas))]

print("\nResultados da análise meteorológica de 2021:")
print(f"A Temperatura média máxima anual é: {media_anual:.2f}°C")
print(f"A Quantidade de meses escaldantes foi: {meses_escaldantes}")
print(f"O Mês mais escaldante do ano foi: {mes_mais_quente} com {max(temperaturas)}°C")
print(f"O Mês menos quente do ano foi: {mes_menos_quente} com {min(temperaturas)}°C")