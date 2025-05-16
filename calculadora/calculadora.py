def soma(x, y):
  return x + y

def subtracao(x, y):
  return x - y

def multiplicacao(x, y):
  return x * y

def divisao(x, y):
  if y == 0:
    return "Erro: Divisão por zero"
  return x / y

def menu():
  print("Escolha a operação:")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")

menu()

op = input("Digite sua opção (1/2/3/4): ")

try:
  a = float(input("Digite o primeiro número: "))
  b = float(input("Digite o segundo número: "))
except ValueError:
  print("Erro: Entrada inválida")
  exit()

if op == '1':
  print("Resultado:", soma(a, b))
elif op == '2':
  print("Resultado:", subtracao(a, b))
elif op == '3':
  print("Resultado:", multiplicacao(a, b))
elif op == '4':
  print("Resultado:", divisao(a, b))
else:
  print("Opção inválida")
