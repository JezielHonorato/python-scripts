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

def radiciacao(x, y):
    if y == 0:
        return "Erro: Radiciação com expoente zero"
    return x ** (1 / y)

def menu():
    print("\n--- CALCULADORA ---")
    print("1 - Soma: A + B")
    print("2 - Subtração: A - B")
    print("3 - Multiplicação: A * B")
    print("4 - Divisão: A / B")
    print("5 - Potenciação: A ^ B")
    print("6 - Radiciação: A ^ (1/B)")
    print("0 - Sair")

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Entrada inválida. Digite um número.")

def main():
    while True:
        menu()
        try:
            op = int(input("Escolha a operação (0-6): "))
        except ValueError:
            print("Erro: Digite um número entre 0 e 6.")
            continue

        if op == 0:
            print("Encerrando a calculadora. Até logo!")
            break

        if op not in range(1, 7):
            print("Erro: Opção inválida.")
            continue

        a = ler_numero("Digite o primeiro número: ")
        b = ler_numero("Digite o segundo número: ")

        match op:
            case 1:
                resultado = soma(a, b)
            case 2:
                resultado = subtracao(a, b)
            case 3:
                resultado = multiplicacao(a, b)
            case 4:
                resultado = divisao(a, b)
            case 5:
                resultado = potenciacao(a, b)
            case 6:
                resultado = radiciacao(a, b)

        print("Resultado:", resultado)

if __name__ == "__main__":
    main()
