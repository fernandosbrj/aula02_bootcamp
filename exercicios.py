# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
# print(num1 + num2)


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# num = int(input("Digite um número: "))
# resto = num % 5
# print(resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
# print(num1 * num2)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
# divisao_inteira = num1 // num2
# print(divisao_inteira)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num1 = int(input("Digite um número: "))
# print(num1 ** 2)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# import math
# raio = float(input("Digit o raio do círculo: "))
# area = math.pi * raio ** 2
# print(area)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# texto = input("Digite algo: ")
# print(texto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome = input("Digite seu nome completo: ")
# print(nome.upper())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Digite uma frase: ")
# print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma data no formato dd/mm/aaaa: ")
# dia, mes, ano = data.split("/")
# print(f"Dia: {dia}, mês {mes} e ano {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# string1 = input("Digite algo: ")
# string2 = input("Digite outra coisa: ")
# print(string1 + string2)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura

# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# temperatura_celsius = input("Digite a temperatura em Celsius: ")

# try:
#     temperatura_celsius = float(temperatura_celsius)

# except ValueError:
#     print("Digite uma temperatura válida")

# else:
#     temp_fahrenheit = temperatura_celsius * 1.8 + 32
#     print(f"{temperatura_celsius} Celsius é igual a {temp_fahrenheit} Fahrenheit")

# 22: Verificador de Palíndromo

# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# texto = input("Digite algo: ")
# texto_invertido = texto[::-1]

# if texto == texto_invertido:
#     print("É um palíndromo")
# else:
#     print("Não é um palíndromo")

# 23: Calculadora Simples

# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

# num1 = input("Digite um número: ")
# num2 = input("Digite outro número: ")
# operacao = input("Digite uma operação matemática entre '+', '-', '*' ou '/' : ")

# try:
#     num1 = float(num1)
#     num2 = float(num2)
# except ValueError as e:
#     print("Digite um número válido")
#     print(e)

# if operacao == "/":

#     try:
#         divisao = num1 / num2
#     except ZeroDivisionError as e:
#         print("O denominador deve ser diferente de zero.")
#         print(e)
#     else:
#         print(f"O resultado da divisão é: {divisao}")
    
# elif operacao == "+":
#     print(num1 + num2)

# elif operacao == "-":
#     print(num1 - num2)

# elif operacao == "*":
#     print(num1 * num2)

# else:
#     print("Digite uma operação válida. Escolha entre '+', '-', 'x' ou '/' ")

# 24: Classificador de Números

# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica 
# e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

# try:
#     num = float(input("Digite um número: "))
#     if num > 0:
#         print("Positivo")
#     elif num < 0:
#         print("Negativo")
#     else:
#         print("Igual a zero")

# except ValueError as e:
#     print(e)
#     print("Digite um número válido")



# 25: Conversão de Tipo com Validação

# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que 
# cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, 
# imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

# lista = input("Insira uma lista de números separados por vírgula: ")
# lista_separada = lista.split(",")
# lista_nova = []

# try:
#     for item in lista_separada:
#         num = int(item.strip())
#         lista_nova.append(num)

#     print("Lista de inteiros", lista_nova)

# except ValueError as e:
#     print(e)
#     print("Lista inválida")
