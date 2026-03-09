"""try:
  resultado = len(3)
  print(resultado)
except TypeError as e:
  print(e)
else:
  print("Tudo ocorreu bem")
finally:
  print("O importante é participar")"""


numero = int(input("Insira um número: "))
if isinstance(numero, int):
  print("A variável é um inteiro")
else:
  print("A variável não é um inteiro")