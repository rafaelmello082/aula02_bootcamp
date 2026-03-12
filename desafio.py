print("\033c", end="")
try:
  nome = input('Digite seu nome: ')
  nome = nome.strip()
  nome_sem_traco_ponto = nome.lstrip('-').replace('.','')
  if nome.isnumeric() or nome_sem_traco_ponto.isnumeric():
    print("Você digitou um número...")
  elif nome == '':
    print("Você não digitou nada...")
  else:
    salario = float(input('Digite seu salário: '))
    perc = float(input('Digite o percentual: '))
    if salario < 0 or perc < 0:
      print("Pelo menos um dos valores digitados é negativo...")
    else:
      bonus = 1000 + salario * ((perc/100) + 1)
      print(f'\nOlá {nome}!\nSeu salário atual: {salario}\nSeu bônus: {bonus:.2f}')
except ValueError:
  print("Pelo menos um dos valores digitados não é um número válido...")
except KeyboardInterrupt:
  print("\nVocê saiu do programa.")
finally:
  print('Até a próxima!')