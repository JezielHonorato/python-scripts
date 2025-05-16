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

def potenciacao(x, y):
  return x ** y

def raticiacao(x, y):
  return x ** (1/y)


def menu():
  print("Escolha a operação:")
  print("1 - Soma: A + B")
  print("2 - Subtração: A - B")
  print("3 - Multiplicação: A * B")
  print("4 - Divisão: A / B")
  print("5 - Potenciação: A ^ B")
  print("6 - Raticiação: A ^ 1/B")

menu()

try:
  op = int(input("Digite sua opção (1/2/3/4/5/6): "))
except ValueError:
  print("Erro: Opção inválida")
  exit()
  
try:
  a = float(input("Digite o primeiro número: "))
  b = float(input("Digite o segundo número: "))
except ValueError:
  print("Erro: Entrada inválida")
  exit()

match op:
  case 1:
    print("Resultado:", soma(a, b))
  case 2:
    print("Resultado:", subtracao(a, b))
  case 3:
    print("Resultado:", multiplicacao(a, b))
  case 4:
    print("Resultado:", divisao(a, b))
  case 5:
    print("Resultado:", potenciacao(a, b))
  case 6:
    print("Resultado:", raticiacao(a, b))
  case _:
    print("Opção inválida")
