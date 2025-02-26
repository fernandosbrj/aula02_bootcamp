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

# 22: Verificador de Palíndromo

# texto = input("Digite algo: ")
# texto_invertido = texto[::-1]

# if texto == texto_invertido:
#     print("É um palíndromo")
# else:
#     print("Não é um palíndromo")

# 23: Calculadora Simples

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
operacao = input("Digite uma operação matemática entre '+', '-', 'x' ou '/' : ")

try:
    num1 = float(num1)
    num2 = float(num2)

except TypeError as e:
    print(e)

try:
    if operacao == "+":
        print(num1 + num2)

    if operacao == "-":
        print(num1 - num2)

    if operacao == "x":
        print(num1 * num2)

    if operacao == "/":
        print(num1 / num2)

except:
    print("Digite uma operação válida. Escolha entre '+', '-', 'x' ou '/' ")


# 24: Classificador de Números

# 25: Conversão de Tipo com Validação