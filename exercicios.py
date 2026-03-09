import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
"""num1 = int(input("Digite o 1o número: "))
num2 = int(input("Digite o 2o número: "))
print(f'A soma dos números digitados é {num1 + num2}')"""

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
"""numero = int(input('Digite um número inteiro qualquer: '))
print(f'O resto da divisão do número digitado por 5 é {numero % 5}')"""

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
"""num1 = int(input("Digite o 1o número: "))
num2 = int(input("Digite o 2o número: "))
print(f'O resultado da multiplicação dos números digitados é {num1 * num2}')"""

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
"""try:
  num1 = int(input('Digite o 1o número: '))
  num2 = int(input('Digite o 2o número: '))
  div_inteira = num1 // num2
  print(f'A divisão inteira dos dois números é {div_inteira}')
except ZeroDivisionError:
  print('Você dividiu por zero')
except ValueError:
  print('Um ou mais valores digitados não é um número inteiro')
except KeyboardInterrupt:
  print('Você escolheu sair do programa...')"""

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
"""numero = int(input('Digite um número inteiro qualquer: '))
print(f'O quadrado do número digitado é {numero ** 2}')"""

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
"""fl1 = float(input("Digite o 1o número: "))
fl2 = float(input("Digite o 2o número: "))
print(f'A soma dos números digitados é {fl1 + fl2}')"""

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
"""fl1 = float(input("Digite o 1o número: "))
fl2 = float(input("Digite o 2o número: "))
print(f'A soma dos números digitados é {(fl1 + fl2)/2}')"""

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
"""base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
resultado = base ** expoente
print(f'O número {base} elevado ao expoente {expoente} é igual a {resultado:.2f}')"""

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
"""temp_celsius = float(input("Digite uma temperatura em celsius: "))
temp_fahrenheit = (temp_celsius * 1.8) + 32
print(f'A temperatura digitada convertida para Fahrenheit é {temp_fahrenheit}')"""

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
"""raio = float(input("Digite o raio: "))
area_circulo = math.pi * raio**2
print(f'Área do círculo: {area_circulo:.2f}')"""

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
"""print("\033c", end="")
palavra = input("Digite uma palavra qualquer: ")
print(f"A palavra digitada em maiúsculas é: {palavra.upper()}")"""

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
"""print("\033c", end="")
palavra = input("Digite uma palavra qualquer: ")
print(f"A palavra digitada em maiúsculas é: {palavra.lower()}")"""

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
"""print("\033c", end="")
frase = input("Digite uma frase qualquer: ")
print(f"Mesma frase sem espaços vazios no início e no fim: \n{frase.strip()}")"""

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
"""print("\033c", end="")
data_inicial = input('Insira uma data no formato "dd/mm/aaaa": ')
data_final = data_inicial.split('/')

print(f'Dia digitado: {data_final[0]}\nMês digitado: {data_final[1]}\nAno digitado: {data_final[2]}')"""

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
"""print("\033c", end="")
str01 = input("Digite a primeira sequência de caracteres: ")
str02 = input("Digite a segunda sequência de caracteres: ")
print(f"As duas sequências que você digitou unidas: {str01 + str02}")"""

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
"""print("\033c", end="")
valor1 = bool(input('Digite o 1o valor: '))
valor2 = bool(input('Digite o 2o valor: '))
print(f'Expressão booleana dos valores digitados: {valor1, valor2}')
print(f'Resultado da operação "AND" entre eles: {valor1 and valor2}')"""

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
"""print("\033c", end="")
valor1 = bool(input('Digite o 1o valor: '))
valor2 = bool(input('Digite o 2o valor: '))
print(f'Expressão booleana dos valores digitados: {valor1, valor2}')
print(f'Resultado da operação "OR" entre eles: {valor1 or valor2}')"""

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
"""print("\033c", end="")
valor = bool(input('Digite um valor qualquer: '))
print(f'Expressão booleana do valor digitado: {valor}')
print(f'O inverso da expressão booleana do valor digitado é: {not valor}')"""

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
"""print("\033c", end="")
num1 = int(input('Digite o 1o número: '))
num2 = int(input('Digite o 2o número: '))
if num1 == num2:
  print("Os números que você digitou são iguais!")
else:
  print("Os números que você digitou são diferentes!")"""

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
"""print("\033c", end="")
num1 = int(input('Digite o 1o número: '))
num2 = int(input('Digite o 2o número: '))
if num1 != num2:
  print("Os números que você digitou são diferentes!")
else:
  print("Os números que você digitou são iguais!")"""

# #### try-except e if

# 21: Conversor de Temperatura
"""print("\033c", end="")
try:
  temp_celsius = float(input("Digite uma temperatura em celsius: "))
  temp_fahrenheit = (temp_celsius * 1.8) + 32
  print(f'A temperatura digitada convertida para Fahrenheit é {temp_fahrenheit:.2f}')
except ValueError:
  print("O valor digitado possui um ou mais caracteres inválidos...")
except KeyboardInterrupt:
  print("\nVocê saiu do programa.")
else:
  print("Programa executado corretamente.")
finally:
  print("Até a próxima!")"""

# 22: Verificador de Palíndromo
"""print("\033c", end="")
try:
  palavra = input("Digite uma palavra qualquer: ")
  palindromo = palavra[::-1]
  if palavra == palindromo:
    print("Você digitou um palíndromo!")
  else:
    print("A palavra digitada não é um palíndromo.")
except ValueError:
  print("Pelo menos um dos caracteres digitados não é uma letra...")
except KeyboardInterrupt:
  print("\nVocê saiu do programa.")
finally:
  print("Até a próxima!")"""

# 23: Calculadora Simples
"""print("\033c", end="")

try:
  op = input("Digite um operador \n(opções: + - * /): ")
  if op != "+" and op != "-" and op != "*" and op != "/":
    print("Operador inválido :(")
  else:
    num1 = float(input('Digite o 1o número: '))
    num2 = float(input('Digite o 2o número: '))

    if op == "+":
      print(f"Resultado de {num1} {op} {num2} = {(num1 + num2):.2f}")
    elif op == "-":
      print(f"Resultado de {num1} {op} {num2} = {(num1 - num2):.2f}")
    elif op == "*":
      print(f"Resultado de {num1} {op} {num2} = {(num1 * num2):.2f}")
    elif op == "/":
      print(f"Resultado de {num1} {op} {num2} = {(num1 / num2):.2f}")
except ValueError:
  print("Pelo menos um dos números que você digitou é inválido...")
except ZeroDivisionError:
  print("Dividir por zero é impossível!")
except KeyboardInterrupt:
  print("\nVocê saiu do programa.")
finally:
  print("Até a próxima!")"""
  
# 24: Classificador de Números
"""print("\033c", end="")
try:
  num = float(input('Digite um número qualquer: '))
  if (num > 0):
    print("Você digitou um número maior que zero!")
  elif (num == 0):
    print("Você digitou o número zero!")
  else:
    print("Você digitou um número menor que zero!")
  if (num % 2 == 0):
    print("Você digitou um número par!")
  else:
    print("Você digitou um número ímpar!")
except ValueError:
  print("Você não digitou um número válido...")
except KeyboardInterrupt:
  print("\nVocê saiu do programa.")"""

# 25: Conversão de Tipo com Validação
print("\033c", end="")
try:
  lista_string = input("Digite uma lista de números, separados por vírgulas: ")
  lista_string = lista_string.split(',')
  lista_int = []
  for i in lista_string:
    lista_int.append(int(i))
  print(lista_int)
except ValueError:
  print("Pelo menos um dos valores digitados não é um número inteiro...")
except KeyboardInterrupt:
  print("\nVocê saiu do programa.")