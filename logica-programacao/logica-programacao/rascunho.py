import math
import random
import string

# print("Hello World, My Firts Program in Python")

# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# print("Soma:", str(valor1 + valor2))

# print("Informe o primeiro valor:")
# valor1 = int(input())
# print("Informe o segundo valor:")
# valor2 = int(input())
# print("Soma:", valor1 + valor2)

#  • int: representa os números inteiros
#  • float: chamado de ponto flutuante representa os números reais
#  • str: chamado de string representa cadeias de caracteres
#  • bool: chamado de booleano representa os valores lógicos true e false

# 1.(False) n#
# 2.(False) 30
# 3.(True) numero1
# 4.(False) idade do aluno
# 5.(True) notaDaP1
# 6.(False) 3valor
# 7.(False) bool
# 8.(False) %
# 9.(True) dia
# 10.(True) endereço
# 11.(True) média
# 12.(False) dia-da-semana
# 13.(True) dia_de_estudar

# 1.(Float) 1.0
# 2.(Int) 1
# 3.(Str) "1"
# 4.(Str) '1'
# 5.(Str) 'C'
# 6.(Bool) True
# 7.(Str) '0.0'
# 8.(-) Rua
# 9.(Str) 'Av. Ipiranga, 6681'
# 10.(Int) 5
# 11.(Str) "João"
# 12.(Float) 4.78
# 13.(Str) "False"

# Operadores aritméticos:
    # + : adição
    # - : subtração
    # * : multiplicação
    # ** : potenciação 2**3 = 8 (Potenciação = 2³)
    # / : divisão real 7/2 = 3.57/2 = 3.5
    # // : divisão inteira 7//2 = 3
    # % : resto de divisão inteira 7%2= 1

# Precedência (ordem de avaliação):
    # ( )
    # **
    # *, /, //, %
    # + e -

# 5+10**2 = 105
# 1-3/4 = 0.25
# 2-3//4 = 2
# 3-4*2 = -5
# 5*(3-4)+1 = -4
# 2**(1+3) = 16
# 7+6%10 = 13
# 7+3*2**(5-3) = 19

# 3+8%5+4*5-10/4+8//5+(3-1)*(2**2)-1
# 3+8%5+4*5-10/4+8//5+2*4-1
# 3+3+20-2.5+1+8-1
# 31.5

# 5+2*(6-2)+6//10+6/10-6%10+3*4
# 5+2*4+6//10+6/10-6%10+3*4
# 5+8+0+0.6-6+12
# 19.6

# 8-12//7+12%7-4*(10%8)-6.0/5+3
# 8-12//7+12%7-4*2-6.0/5+3
# 8-1+5-8-1.2+3
# 5.8

#  • Raiz quadrada √: math.sqrt(x)
#  • Potenciação 𝑥𝑦: math.pow(x,y)
#  • Módulo |x|: math.fabs(x)
#  • Fatorial x!: math.factorial(x)
#  • Maior divisor comum: math.gdc(x,y)
#  • Arredonda para o próximo inteiro: math.ceil(x)
#  • Trunca para inteiro : math.trunch(x)
#  • Funções trigonométricas: math.sin(x), math.cos(x), ...
#  • Constante PI π: math.pi

#  • Raiz quadrada √: math.sqrt(x)
    # x = 10
    # resultado = math.sqrt(2*x)
    # print(resultado)
    # b = 10
    # a = 1
    # c = 1
    # resultado = math.sqrt(b*b-4*a*c)
    # print(resultado)

#  • Potenciação 𝑥𝑦: math.pow(x,y)
    # b = 10
    # a = 1
    # c = 1
    # resultado = math.pow(b,2*a+c)
    # print(resultado)
    # resultado = math.sqrt(math.pow(b,2)-4*a*c)
    # print(resultado)

#  • Módulo |x|: math.fabs(x)
    # b = 1
    # a = 1
    # c = 3
    # resultado = math.fabs(math.pow(b,3)-10)
    # print(resultado)
    # resultado = math.fabs(a-2*c)
    # print(resultado)

#  • Fatorial x!: math.factorial(x)
    # a = 5
    # n = 3
    # p = 2
    # resultado = math.factorial(a)
    # print(resultado)
    # resultado = math.factorial(n)/(math.factorial(n-p)*math.factorial(p))
    # print(resultado)

#  • Maior divisor comum: math.gdc(x,y)
    # a = 10
    # b = 15
    # resultado = math.gcd(a,b)
    # print(resultado)

#  • Arredonda para o próximo inteiro: math.ceil(x)
    # print(math.ceil(9.1))
    # print(math.ceil(9.8))
    # print(math.ceil(9.5))

#  • Trunca para inteiro : math.trunch(x)
    # print(math.trunc(9.1))
    # print(math.trunc(9.8))
    # print(math.trunc(9.5))

#  • Funções trigonométricas: math.sin(x), 
    # print(math.sin(1))
    # print(math.sin(90))
    # print(math.sin(180))

#  • Funções trigonométricas: math.cos(x), ...
    # print(math.cos(1))
    # print(math.cos(90))
    # print(math.cos(180))

#  • Constante PI π: math.pi
# print(math.pi)

# num = 10
# num = 20
# num = num+2
# num = num+3
# num = num//2 
# num = 2+(num-10)*2
# print(num) = 6

# val = 7
# val = 9//4
# val = val+1
# val = val+10
# val = 4+val–5*2
# val = val//2
# val = math.abs(val–19)+2
# print(val) = 18

# print("Informe quantos fahrenheit deseja converter para celsius:")
# fahrenheit = float(input())
# celsius = (fahrenheit - 32) * 5/9
# print("O valor em celsius é:", celsius)

# print("digite o primeiro valor:")
# v1 = int(input())
# print("digite o segundo valor:")
# v2 = int(input())
# print("A soma dos valores é:", v1 + v2)
# print("A diferença dos valores é:", abs(v1 - v2))
# print("A média dos valores é:", (v1 + v2) / 2)
# print("A distância entre os valores é:", abs(v1 - v2))
# print("O maior valor é:", max(v1, v2))
# print("O menor valor é:", min(v1, v2))

# print("Informe o tempo em segundos:")
# segundos = int(input())
# horas = segundos // 3600
# segundos = segundos % 3600
# minutos = segundos // 60
# segundos = segundos % 60
# print("O tempo é: ", horas, "h", minutos, "m", segundos, "s")

# print("Informe o valor inteiro de 4 dígitos:")
# valor = int(input())
# milhar = valor // 1000
# valor = valor % 1000
# centena = valor // 100
# valor = valor % 100
# dezena = valor // 10
# unidade = valor % 10
# print(milhar,unidade,dezena,centena)

# Expressões Lógicas 
# São aquelas que resultam em true ou false.
# Para definir expressões lógicas, usamos operadores:
#  • Relacionais: >, <, >=, <=, !=, ==
    # • Exemplos:
    # • 3>5 false
    # • 10<=10 true
    # • 5!=5 false
    # • 2==2 true

#  • Lógicos: and(E), or(ou) e not(não)
    # • Exemplos:
    # • 3>5 and 10<=10 false = Os dois valores precisam ser verdadeiros
    # • 10<=10 or 5!=5 true = Pelo menos um valor precisa ser verdadeiro
    # • not 2==2 false = Inverte o valor lógico

# num1 = int(input("Digite o primeiro número:"))
# num2 = int(input("Digite o segundo número:"))
# num3 = int(input("Digite o terceiro número:"))
# num = num1>0
# print(num)
# num = num3>=0 and num3%2==0
# print(num)

# num1 = int(input("Digite o primeiro número:"))
# num2 = int(input("Digite o segundo número:"))
# num3 = int(input("Digite o terceiro número:"))
# num = num3>=0 and num3<=10
# print(num3,"está entre 0 e 10?", num)
# num = num1<0 and num1>10
# print(num3,"não está entre 0 e 10?", num)
# num = num2>num1 and num2>num3
# print(num2, "é o maior valor?", num)
# num = num2%7==0
# print(num2, "é divisível por 7?", num)
# num = num2%num3==0 or num3%num2==0
# print(num2, "e", num3, "são multiplos?", num)
# num = num1==num2 and num2==num3 and num3==num1
# print("Os números são iguais?", num)
# num = num1==num2 or num2==num3 or num3==num1
# print("2 dos valores são iguais?", num)

# valor = int(input("Digite um valor:"))
# if valor>0: print("O valor é positivo")
# if valor<0: print("O valor é negativo")
# if valor==0: print("O valor é Zero")

# valor = int(input("Digite um valor:"))
# if valor>0:
#     print("O valor é positivo")
# if valor<0:
#     print("O valor é negativo")
# if valor==0:
#     print("O valor é Zero")

# print("Informe o primeiro valor:")
# v1 = int(input())
# print("Informe o segundo valor:")
# v2 = int(input())
# print("Informe o terceiro valor:")
# v3 = int(input())
# if v1>v2 and v1>v3:
#     print("O maior valor é:", v1)
# if v2>v1 and v2>v3:
#     print("O maior valor é:", v2)
# if v3>v1 and v3>v2:
#     print("O maior valor é:", v3)
    
# print("Informe o primeiro valor:")
# v1 = int(input())
# print("Informe o segundo valor:")
# v2 = int(input())
# print("Informe o terceiro valor:")
# v3 = int(input())
# if v1>v2 and v1>v3: maior = v1
# if v2>v1 and v2>v3: maior = v2
# if v3>v1 and v3>v2: maior = v3
# print("O maior valor é:", maior)

# print("Informe o primeiro valor:")
# v1 = int(input())
# print("Informe o segundo valor:")
# v2 = int(input())
# if v1>v2:
#     print(v1,v2)
# else:
#     print(v2,v1)

# print("Informe o primeiro valor:")
# v1 = int(input())
# print("Informe o segundo valor:")
# v2 = int(input())
# if v1>v2:
#     aux = v1
#     v1 = v2
#     v2 = aux
#     print(v1,v2)

# valor = int(input("Informe um valor:"))
# if valor>0:
#     print("O valor é positivo")
# else:
#     print("O valor é negativo")

# altura = float(input("Informe a altura: "))
# if altura <= 0:
#     print("Altura inválida, Recarregue o programa e informe um valor válido")
# else: genero = str(input("Informe seu genero: Masculino ou Feminino "))
# if genero == "Masculino":
#     peso = 72.7*altura-58
#     print("Seu peso ideal é:", peso)
# if genero == "Feminino":
#     peso = 52.1*altura-44.7
#     print("Seu peso ideal é:", peso)
# if genero != "Masculino" and genero != "Feminino":
#     print("Gênero inválido, Recarregue o programa e informe um genero válido")

# altura = float(input("Informe a altura: "))
# 
# if altura > 0:
#     
#     genero = str(input("Informe seu genero: Masculino ou Feminino "))
#     
#     if genero == "Masculino":
#         peso = 72.7*altura-58
#         print("Seu peso ideal é:", peso)
#     
#     if genero == "Feminino":
#         peso = 52.1*altura-44.7
#         print("Seu peso ideal é:", peso)
#     
#     if genero != "Masculino" and genero != "Feminino":
#         print("Gênero inválido, Recarregue o programa e informe um genero válido")
#           
# else: print("Altura inválida, Recarregue o programa e informe um valor válido")

# mana = float(input("Informe nível de mana de 0 a 10: "))
# 
# if mana >= 0 or mana <= 10:
#     
#     if mana >= 9 and mana <= 10: print("Seu Rank S")
#     if mana >= 7 and mana < 9: print("Seu Rank A")
#     if mana >= 5 and mana < 7: print("Seu Rank B")
#     if mana >= 3 and mana < 5: print("Seu Rank C")
#     if mana >= 1 and mana < 3: print("Seu Rank D")
#     if mana == 0: print("Seu Rank E")
#     
# else: print("Nível de Mana inválido, Recarregue o programa e informe um nível válido")

# horaInicial = int(input("Informe a hora inicial: "))
# minutoInicial = int(input("Informe o minuto inicial: "))
# horaFinal = int(input("Informe a hora final: "))
# minutoFinal = int(input("Informe o minuto final: "))
# 
# horaInicial = horaInicial*60+minutoInicial
# horaFinal = horaFinal*60+minutoFinal
# 
# if horaInicial < horaFinal: duracao = horaFinal - horaInicial
# 
# else: duracao = 24 * 60 - horaInicial + horaFinal
# 
# print("A duração do jogo foi de", duracao//60, "horas e", duracao%60, "minutos")

# num = int(input("Informe um valor inteiro de 4 digitos: "))
# 
# if num < 1111 or num > 9999:
#     print("Valor inválido, recarregue o programa e informe um valor válido")
# 
# else:
#     milhar = num // 1000
#     resto = num % 1000
#     centena = resto // 100
#     resto = resto % 100
#     dezena = resto // 10
#     unidade = resto % 10
#     invertido = unidade*1000+dezena*100+centena*10+milhar
#     
#     print("O valor invertido é:", invertido)
#     
#     if num == invertido:
#         print("O valor é uma Capicua")
#     else:
#         print("O valor não é Capicua")

# v1 = int(input("Informe o primeiro valor: "))
# v2 = int(input("Informe o segundo valor: "))
# v3 = int(input("Informe o terceiro valor: "))
# 
# if v1 > v2 and v1 > v3:
#     maior = v1
# elif v2 > v1 and v2 > v3:
#     maior = v2
# else:
#     maior = v3
# 
# if v1 < v2 and v1 < v3:
#     menor = v1
# elif v2 < v1 and v2 < v3:
#     menor = v2
# else:
#     menor = v3
# 
# if (v1 != maior and v1 != menor):
#     meio = v1
# elif (v2 != maior and v2 != menor):
#     meio = v2
# else:
#     meio = v3
# 
# print("O maior valor é:", maior)
# print("O valor do meio é:", meio)
# print("O menor valor é:", menor)

# preco = float(input("Informe o Preço de Custo do Produto: "))
# 
# if preco > 0 and preco <= 10:
#     preco = preco * 1.7
#     
# elif preco > 10 and preco <= 30:
#     preco = preco * 1.5
#     
# elif preco > 30 and preco <= 50:
#     preco = preco * 1.4
#     
# else:
#     preco = preco * 1.3
# 
# print("O Valor de Venda é:", preco)	

# dia = int(input("Informe o dia da semana: "))
# 
# if dia == 1:
#     print("Domingo")
# elif dia == 2:
#     print("Segunda")
# elif dia == 3:
#     print("Terça")
# elif dia == 4:
#     print("Quarta")
# elif dia == 5:
#     print("Quinta")
# elif dia == 6:
#     print("Sexta")
# elif dia == 7:
#     print("Sábado")
# else:
#     print("Dia inválido")

# n1 = int(input("Informe a primeira nota: "))
# n2 = int(input("Informe a segunda nota: "))
# n3 = int(input("Informe a terceira nota: "))
# 
# if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
#     print("Nota inválida, recarregue o programa e informe uma nota válida")
# 
# if n1 > n2 and n1 > n3:
#     maior = n1
# elif n2 > n1 and n2 > n3:
#     maior = n2
# else:
#     maior = n3
#     
# media = 0.5 * maior + 0.25 * (n1+n2+n3-maior)
# 
# print("Média Ponderada:", media)

# saldo = float(input("Informe o saldo da conta: "))
# 
# if saldo >= 0 and saldo < 500:
#     print("Não há limite disponível")
# elif saldo >= 500 and saldo < 1000:
#     limite = (saldo*1.08)-saldo
#     print("O limite disponível é de R$", limite)
# elif saldo >= 1000:
#     limite = (saldo*1.15)-saldo
#     print("O limite disponível é de R$", limite)
# else:
#     print("Saldo inválido, recarregue o programa e informe um saldo válido")

# a = float(input("A: "))
# b = float(input("B: "))
# c = float(input("C: "))
# 
# delta = b**2 - 4*a*c
# 
# if delta < 0:
#     print("A equação não possui raízes reais")
# elif delta == 0:
#     x = -b/(2*a)
#     print(f"A equação possui uma raiz real: {x}")
# else:
#     x1 = (-b + math.sqrt(delta))/(2*a)
#     x2 = (-b - math.sqrt(delta))/(2*a)
#     print(f"A equação possui duas raízes reais: {x1} e {x2}")

# temp = float(input("Informe a temperatura em Celsius: "))
# umid = float(input("Informe a umidade relativa do ar: "))
# 
# if temp > 40 and umid >= 60:
#     print("Muito Quente e Úmido")
# elif temp > 40 and umid < 60:
#     print("Muito Quente e Seco")
# elif temp > 30 and umid >= 60:
#     print("Quente e Úmido")
# elif temp > 30 and umid < 60:
#     print("Quente e Seco")
# elif temp > 20 and temp <= 30 and umid >= 60:
#     print("Ameno e Úmido")
# elif temp > 20 and temp <= 30 and umid < 60:
#     print("Ameno e Seco")
# elif temp > 10 and temp <= 20 and umid >= 60:
#     print("Frio e Úmido")
# elif temp > 10 and temp <= 20 and umid < 60:
#     print("Frio e Seco")
# elif temp <= 10 and umid >= 60:
#     print("Muito Frio e Úmido")
# elif temp <= 10 and umid < 60:
#     print("Muito Frio e Seco")
# else:
#     print("Valores inválidos, recarregue o programa e informe valores válidos")

# nota1 = float(input("Informe a primeira nota: "))
# nota2 = float(input("Informe a segunda nota: "))
# nota3 = float(input("Informe a terceira nota: "))
# 
# freq = float(input("Informe sua frequência de presença: "))
# 
# if freq > 0 and freq < 75:
#     print("Reprovado por falta")
# elif freq >= 75 and freq <= 100:
#     
#     media = (nota1 + nota2 + nota3) / 3
# 
#     if media >= 7:
#         print("Aprovado em Grau 1")
#     elif media >= 4:
#         print("Recuperação, devera fazer a prova de Grau 2")
#         
#         nota1 = float(input("Informe a primeira nota da recuperação: "))
#         nota2 = float(input("Informe a segunda nota da recuperação: "))
#         nota3 = float(input("Informe a terceira nota da recuperação: "))
#         
#         media = (nota1 + nota2 + nota3) / 3
#         
#         if media >= 5:
#             print("Aprovado em Grau 2")      
#         else:
#             print("Reprovado em Grau 2")
#             
#     else:
#         print("Reprovado")
# else:
#     print("Frequência inválida, recarregue o programa e informe uma frequência válida")
    
# nota = float(input("Informe sua nota: "))
# 
# if nota >= 0 or nota <= 10:
#     
#     if nota >= 9 and nota <= 10:
#         print("Conceito A")
#     elif nota >= 8 and nota < 9:
#         print("Conceito B")
#     elif nota >= 7 and nota < 8:
#         print("Conceito C")
#     elif nota >= 6 and nota < 7:
#         print("Conceito D")
#     else:
#         print("Conceito E")
#     
# else: print("Nota inválida, Recarregue o programa e informe uma nota válida")

# ano = int(input("Informe o ano que você deseja saber a data da Páscoa: "))
# 
# a = ano % 19
# b = ano // 100
# c = ano % 100
# d = b // 4
# e = b % 4
# f = (b + 8) // 25
# g = (b - f + 1) // 3
# h = (19 * a + b - d - g + 15) % 30
# i = c // 4
# k = c % 4
# l = (32 + 2 * e + 2 * i - h - k) % 7
# m = (a + 11 * h + 22 * l) // 451
# mes = (h + l - 7 * m + 114) // 31
# dia = ((h + l - 7 * m + 114) % 31) + 1
# 
# meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
# 
# print(f"O Domingo de Páscoa será no dia {dia} de {meses[mes-1]} de {ano}")

# mes = int(input("Informe o mês: "))
# 
# if mes == 2:
#     dias = 28
# elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
#     dias = 30
# else:
#     dias = 31
# 
# print(f"O mês {mes} possui {dias} dias")

# altura = float(input("Informe a altura: "))
# 
# if altura <= 0:
#     print("Altura inválida, Recarregue o programa e informe um valor válido")
#     
# else:
#     genero = str(input("Informe seu genero: Masculino ou Feminino "))
#     
#     if genero == "Masculino":
#         peso = 72.7*altura-58
#         print("Seu peso ideal é {peso}")
#     elif genero == "Feminino":
#         peso = 52.1*altura-44.7
#         print("Seu peso ideal é {peso}")
#     else:
#         print("Gênero inválido, Recarregue o programa e informe um genero válido")
        
# altura = float(input("Informe a altura: "))
# peso = float(input("Informe o peso: "))
# 
# imc = peso / altura**2
# 
# print(f"Seu IMC é {imc}")
# 
# if imc < 18.6:
#     print("Abaixo do Peso")
# elif imc < 25:
#     print("Peso Ideal")
# elif imc < 30:
#     print("Sobrepeso")
# elif imc < 35:
#     print("Obesidade Grau I")
# elif imc < 40:
#     print("Obesidade Grau II")
# else:
#     print("Obesidade Grau III")



# jogador = (input("[Pedra], [Papel] ou [Tesoura]? "))
# computador = random.choice(["Pedra", "Papel", "Tesoura"])
# 
# print(f"O computador escolheu {computador}")
# 
# if jogador == computador:
#     print(f"Você jogou {jogador} e o Computador jogou {computador}, Deu Empate!")
#     
# elif jogador == "Pedra":
#     if computador == "Tesoura":
#         print(f"{jogador} quebra {computador}, Jogador Vence!")
#     else:
#         print(f"{computador} cobre {jogador}, Computador Vence!")
# 
# elif jogador == "Papel":
#     if computador == "Pedra":
#         print(f"{jogador} embrulha {computador}, Jogador Vence!")
#     else:
#         print(f"{computador} corta {jogador}, Computador Vence!")
#         
# elif jogador == "Tesoura":
#     if computador == "Papel":
#         print(f"{jogador} corta {computador}, Jogador Vence!")
#     else:
#         print(f"{computador} quebra {jogador}, Computador Vence!")
#         
# else:
#     print("Jogada Inválida")

# sist = int(input("Sistólica: "))
# diast = int(input("Diastólica: "))
# 
# if sist < 120 and diast < 80:
#     print("Pressão Normal")
# elif sist < 130 and diast < 80:
#     print("Pré-Hipertensão")
# elif sist < 140 and diast < 90:
#     print("Hipertensão Grau I")
# elif sist < 180 and diast < 120:
#     print("Hipertensão Grau II")
# else:
#     print("Crise Hipertensiva")

# ano = int(input("Informe o ano: "))
# 
# if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
#      print("Ano Bissexto")
# 
# else:
#     print("Ano Não Bissexto")
    
# mes = int(input("Informe o mês: "))
# ano = int(input("Informe o ano: "))
# 
# if mes == 2:
#     if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
#         dias = 29
#     else:
#         dias = 28
#         
# elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
#     dias = 30
#     
# else:
#     dias = 31
# 
# print(f"O mês {mes} possui {dias} dias")

# bruto = float(input("Informe o salário bruto: "))
# dependentes = int(input("Informe o número de dependentes: "))
# 
# if bruto < 1212.01:
#     alinss = bruto * 0.075
#     parcinss = 0
# elif bruto <= 2427.35:
#     alinss = 0.09
#     parcinss = 18.18
# elif bruto <= 3641.03:
#     alinss = 0.12
#     parcinss = 91
# else:
#     alinss = 0.14
#     parcinss = 163.82
#     
# inss = alinss * bruto - parcinss
# 
# if inss > 828.39:
#     inss = 828.39
#     
# print(f"INSS: {inss}")
# 
# base = bruto - inss - 189.59 * dependentes
# 
# if base < 1903.99:
#     aliqirrf = 0
#     parcirrf = 0
# elif base <= 2826.65:
#     aliqirrf = 0.075
#     parcirrf = 142.80
# elif base <= 3751.05:
#     aliqirrf = 0.15
#     parcirrf = 354.80
# elif base <= 4664.68:
#     aliqirrf = 0.225
#     parcirrf = 636.13
# else:
#     aliqirrf = 0.275
#     parcirrf = 869.36
#     
# irrf = base * aliqirrf - parcirrf
#     
# print(f"IRRF: {base * aliqirrf - parcirrf}")
# 
# liquido = bruto - inss - irrf
# 
# print(f"Salário Líquido: {liquido}")

# Contagem progressiva, do 0 ao 10, quando chega no 9, o laço termina
# for cont in range(10):
#    print(cont)

# Contagem progressiva, do 1 ao 12, porem adicionando 2 a cada iteração, quando chegar no 11, o laço termina
# for cont in range(1,12,2):
#     print(cont)

# Contagem regressiva, do 10 ao 0, subtraindo 1 a cada iteração, quando chegar no 1, o laço termina
# for cont in range(10,0,-1):
#     print(cont)

# Contagem progressiva monstrando a raiz quadrada de cada número de 1 a 50
# for num in range(1,51):
#     print(f"{num}: {math.sqrt(num)}")
# Contagem progressiva monstrando a raiz quadrada de cada número de 1 a 50, com 3 casas decimais
# for num in range(1,51):
#     print(f"{num:6}: {math.sqrt(num):.3f}")

# soma = 0
# num = int(input("Informe um número: "))
# 
# for cont in range(1,num+1):
#     soma = soma + cont
#     
#     print(f"{cont} + {soma}: {cont + soma}")
#     
# print(f"A soma dos números de 1 a {num} é {soma}")

# num = int(input("Valor desejado: "))
# total = int(input("Qtd. de Repetições: "))
# 
# aprox = 1
# 
# for cont in range(1,total+1):
#     aprox = (aprox + num/aprox) / 2
#     print(f"{cont:3} {aprox:.5f}")
#     
# print(f"A raiz quadrada de {num} é aproximadamente {aprox:.5f}")

# for cont in range(20):
#     if cont > 10:
#         break
#     print(cont)
# print("Fim do laço")

# for cont in range(20):
#     if cont % 2 == 1:
#         continue
#     print(cont)
# print("Fim do laço")

# for cont in range(13):
#     mes = int(input("Informe o mês: "))
#     print(mes)
# print("Fim do laço")

# num = int(input("Valor desejado: "))
# total = int(input("Qtd. de Repetições: "))
# 
# aprox = 1
# anterior = 0
# 
# for cont in range(1,total+1):
#     aprox = (aprox + num/aprox) / 2
#     print(f"{cont:3} {aprox:.5f}")
#     dif = abs(aprox - anterior)
#     if dif < 0.001:
#         break
#     anterior = aprox
# 
# print(f"A raiz quadrada de {num} é aproximadamente {aprox:.5f}")

# soma = 0
# 
# for cont in range(10):
#     
#     alt = float(input("Informe a altura: "))
#     soma = soma + alt
#     
# media = soma / 10
# 
# print(f"A média das alturas é {media:.3f}")

# soma = 0
# maior = 0
# 
# for cont in range(10):
#     
#     alt = random.uniform(1.5,2.10)
#     soma = soma + alt
#     
#     if alt > maior:
#         maior = alt
#     
# media = soma / 10
# 
# print(f"A média das alturas é {media:.3f}")
# print(f"A maior altura é {maior:.3f}")

# somaIdades = 0
# cursoMaisVelho = " "
# idadeMaisVelho = 0
# qtdAlunosSem5oSem = 0
# 
# for cont in range(5):
#     # Sorteio
#     idade = random.randint(18,60)
#     curso = random.choice(["ADS","CC","BD","SI","ES"])
#     
#     semestre = random.randint(1,10)
#     # Coleta de estatísticas
#     # Media de idades: é necessário somar as Idades 
# 
#     somaIdades += idade
#     # Curso do aluno mais velho
#     
#     if idade > idadeMaisVelho:
#         idadeMaisVelho = idade
#         cursoMaisVelho = curso
#     
#     # Total de alunos no 5° semestre
#     if semestre == 5:
#         qtdAlunosSem5oSem += 1
#         
# mediaIdades = somaIdades // 5
#     
# print(f"Média de Idades: {mediaIdades}")
# print(f"Curso do aluno mais velho ({idadeMaisVelho} anos): {cursoMaisVelho}")
# print(f"Total de alunos no 5° semestre: {qtdAlunosSem5oSem}")

# texto = "Hello World"
# 
# print(texto[2])
# print(texto[4])
# print(texto[-4])
# print(texto[-2])
# print(texto[-1])
# print(texto[0:5])
# print(texto[-1:-5])
# print(texto + "." )
# print(texto * 3)
# result = texto * 4 + "!" + "!" * 2
# print(result)
# texto = texto[:5] + " e " + texto[6:]
# print(texto)

# texto = "Hello World"
# texto02 = "Python"
# if texto < texto02:
#     print(f"{texto} vem antes de {texto02}")
# elif texto02 < texto:
#     print(f"{texto02} vem depois de {texto}")
# else:
#     print(f"{texto} é igual a {texto02}")

# text1 = input("Informe uma frase: ")
# text2 = input("Informe uma palavra: ")
# 
# if text2 in text1:
#     print(f"'{text2}' está presente em '{text1}'")
# else:
#     print(f"'{text2}' não está presente em '{text1}'")
#     
# print(f"O comprimento de '{text1}' é de {len(text1)} caracteres")

# text1 = "então apenas a deixei ir, enquanto lembrava de nossos momentos e segurava minha dor de forma sutil - alguem, 2025"
# 
# for caractere in text1:
#     print(caractere)
#     
# for pos in range(len(text1)):
#     print(f"{pos}: {text1[pos]}")

# text = input("Digite uma frase: ")
# 
# dif = False
# 
# for pos in range(len(text)//2):
#     if text[pos] != text[-pos-1]:
#         dif = True
#         break
#     
# if not dif:
#     print("A frase é um palíndromo")
# else:
#     print("A frase não é um palíndromo")
#     
# if text == text[::-1]:
#     print("A frase é um palíndromo")
# else:
#     print("A frase não é um palíndromo")
#     
# vogais = "aeiouAEIOU"
# totalVogais = 0
# 
# for letra in text:
#     if letra in vogais:
#         totalVogais += 1
# 
# print(f"A frase possui {totalVogais} vogais")

# senha = input("Informe uma Senha de 8 Digitos: ")
# 
# maiuscula = False
# digito = False
# pontuacao = False
# 
# if len(senha) >= 8:
#     for letra in senha:
#         if letra in string.ascii_uppercase:
#             maiuscula = True
#             
#         if letra in string.digits:
#             digito = True
#             
#         if letra in string.punctuation:
#             pontuacao = True
#             
#             ## Forma abreviada
#             ## if letra.isupper():
#             ##     maiuscula = True
#             ## if letra.isdigit():
#             ##     digito = True
#             ## if letra in "!@#$%&*":
#             ##     pontuacao = True
#             
#     if maiuscula == False or digito == False or pontuacao == False:
#                 
#         if maiuscula == False:
#             print("Senha não possui letra maiúscula")
#         if digito == False:
#             print("Senha não possui dígito")
#         if pontuacao == False:
#             print("Senha não possui pontuação")
#     else:
#         print("Senha Válida")
# 
# else:
#     print("Senha muito curta")

# nome = input("Informe seu nome: ")
# 
# inicio = True
# 
# for letra in nome:
#     if inicio:
#         print(f"{letra}. ", end="")
#         inicio = False
#     elif letra == " ":
#         inicio = True
#         print()

# sorteado = random.randint(1,100)
# 
# acertou = False
# 
# for tentativa in range(1,11):
#     
#     if tentativa > 0 and tentativa < 11:
#         
#         print(f"Tentativa {tentativa}: ", end="")
#         num = int(input())
#             
#         if num > sorteado:
#             print("Tente um número Menor...")
#         elif num < sorteado:
#             print("Tente um número Maior...")
#         else:
#             acertou = True
#             break
# 
# if acertou:
#     print(f"Parabéns! você acertou em {tentativa} tentativas")
# else:
#     print("Fim de jogo!")
#     print(f"O número sorteado era {sorteado}.")     

# num = int(input("Informe um número: "))
# aux = num
# cont = 0
# d = 1
# 
# while d <= num:
#     
#     if num % d == 0 : cont = cont + 1
#     d = d + 1
# 
# if cont == 2:        
#     print(f"{num} é um número primo")
# 
# else:
#     print(f"{num} não é um número primo")

# nTermos = int(input("Informe o número de termos: "))
# 
# if nTermos <= 0:
#     print("Informe um número positivo")
#     
# else:
#     
#     soma = 0
#     cont = 1
#     numerador = 2
#     denominador = 1
#     
#     while cont <= nTermos:
#         soma = soma + numerador/denominador
#         cont = cont + 1
#         numerador = numerador + 2
#         denominador = denominador + 2
#         
#     print(f"A soma dos {nTermos} termos é {soma:.2f}")

# a = int(input("Informe o primeiro valor: "))
#     
# while a <= 0:
#     print("Informe um número positivo")
#     a = int(input("Informe novamente o primeiro valor: "))
#     
# b = int(input("Informe o segundo valor: "))
#     
# while b <= 0:
#     print("Informe um número positivo")
#     b = int(input("Informe novamente o segundo valor: "))
#         
# if a>b:
#     aux = a
#     a = b
#     b = aux
#             
# if a % 2 == 0:
#     a = a + 1
#     soma = 0
#     print(f"Os números ímpares entre {a} e {b} são:\n {soma}")
#             
# while a<=b:
#     print(a)
#     soma = soma + a
#     a = a + 2
#         
# print(f"A soma dos números ímpares no intervalo é {soma}")

# a = int(input("Informe um valor inteiro: "))
# 
# while a <= 0:
#     print("Informe um número positivo")
#     a = int(input("Informe um valor: "))
#     
# soma = 0
# cont = 1
# 
# while cont < a/2:
#     
#     if a % cont == 0: soma = soma + cont
#     cont = cont + 1    
#         
# if soma == a:
#     print("Número Perfeito")
# else:
#     print("Número Imperfeito")

# altChico = 1.50
# altZe = 1.10
# anos = 0
# 
# while altZe <= altChico:
#     altChico = altChico + 0.02
#     altZe = altZe + 0.03
#     anos = anos + 1
#     
# print(f"Zé demorou {anos} anos, para ficar maior que chico")

