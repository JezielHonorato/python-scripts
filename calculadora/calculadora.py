# Operações Matemáticas


def soma(x, y):
    """Calcula a soma de dois números."""
    return x + y


def subtracao(x, y):
    """Calcula a subtração de dois números."""
    return x - y


def multiplicacao(x, y):
    """Calcula o produto de dois números."""
    return x * y


def divisao(x, y):
    """
    Calcula a divisão de dois números.
    """
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y


def potenciacao(x, y):
    """
    Calcula x elevado à potência y.
    """
    if x == 0 and y == 0:
        return "Erro: 0^0 é uma forma indeterminada."
    return x**y


def radiciacao(x, y):
    """
    Calcula a raiz y-ésima de x (x elevado a 1/y).
    """
    if y == 0:
        return "Erro: O índice da raiz não pode ser zero (não existe a 0ª raiz)."
    if x < 0 and y % 2 == 0:
        return "Erro: Raiz de número negativo com índice par não é um número real."
    return x ** (1 / y)


def equacao_linear(a, b):
    """
    Resolve uma equação de primeiro grau do tipo ax + b = 0.
    """
    if a == 0:
        if b == 0:
            return "A equação tem infinitas soluções (0x + 0 = 0)."
        else:
            return "A equação não possui solução (ex: 0x + 5 = 0 é falso)."
    else:
        x = -b / a
        return f"x = {x:.4f}"


def equacao_quadratica(a, b, c):
    """
    Resolve uma equação de segundo grau do tipo ax^2 + bx + c= 0.
    """
    if a == 0:
        return equacao_linear(b, c)

    delta = (b**2) - (4 * a * c)

    if delta == 0:
        x = -b / (2 * a)
        return f"Uma solução real (ou duas soluções iguais): x = {x:.4f}"
    elif delta > 0:
        delta = delta ** (1 / 2)
        x1 = (-b + delta) / (2 * a)
        x2 = (-b - delta) / (2 * a)
        return f"Duas soluções reais: x1 = {x1:.4f} e x2 = {x2:.4f}"
    else:
        return "Nenhuma solução real (soluções são complexas)."


# Funções de Entrada e Saída do Console


def exibir_menu():
    """Exibe o menu de operações para o usuário."""
    print("\n" + "=" * 40)
    print("      CALCULADORA E RESOLUTOR DE EQUAÇÕES")
    print("=" * 40)
    print("Escolha uma opção:")
    print("  1 - Soma (a + b)")
    print("  2 - Subtração (a - b)")
    print("  3 - Multiplicação (a * b)")
    print("  4 - Divisão (a / b)")
    print("  5 - Potenciação (a ^ b)")
    print("  6 - Radiciação (a ^ (1/b))")
    print("  7 - Equação de Primeiro Grau (ax + b = 0)")
    print("  8 - Equação de Segundo Grau (ax^2 + bx + c = 0)")
    print("  0 - Sair")
    print("=" * 40)


def obter_numero(prompt):
    """
    Solicita o valor ao usuario.
    """
    while True:
        try:
            valor = float(input(prompt))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")


def obter_opcao(limite_superior):
    """
    Solicita a opção ao usuario.
    """
    while True:
        try:
            op = int(input("Digite sua opção: "))
            if 0 <= op <= limite_superior:
                return op
            else:
                print(
                    f"Opção fora do intervalo. Por favor, digite um número entre 0 e {limite_superior}."
                )
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


# Função main


def main():
    while True:
        exibir_menu()
        opcao = obter_opcao(8)

        if opcao == 0:
            print("\nObrigado por usar a calculadora! Até mais!")
            break

        if opcao in [1, 2, 3, 4, 5, 6, 7, 8]:
            print("\n--- Entrada de Números ---")
            if opcao >= 7:
                num1 = obter_numero("Digite o coeficiente 'a': ")
                num2 = obter_numero("Digite o coeficiente 'b': ")
                if opcao == 8:
                    num3 = obter_numero("Digite o coeficiente 'c': ")
            else:
                num1 = obter_numero("Digite o primeiro número: ")
                num2 = obter_numero("Digite o segundo número: ")

            resultado = None

            match opcao:
                case 1:
                    resultado = soma(num1, num2)
                case 2:
                    resultado = subtracao(num1, num2)
                case 3:
                    resultado = multiplicacao(num1, num2)
                case 4:
                    resultado = divisao(num1, num2)
                case 5:
                    resultado = potenciacao(num1, num2)
                case 6:
                    resultado = radiciacao(num1, num2)
                case 7:
                    resultado = equacao_linear(num1, num2)
                case 8:
                    resultado = equacao_quadratica(num1, num2, num3)

            print("\n" + "-" * 40)
            if isinstance(resultado, str) and "Erro:" in resultado:
                print(f"ERRO: {resultado}")
            else:
                print(f"RESULTADO: {resultado}")
            print("-" * 40)
            input("\nPressione Enter para continuar...")
        else:
            print("Opção inválida. Por favor, escolha uma opção do menu.")


if __name__ == "__main__":
    main()
