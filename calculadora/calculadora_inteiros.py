# Todas as operações matemticas são somas.

def soma(x, y):
    """Calcula a soma de dois números."""
    return x + y

def subtracao(x, y):
    """Calcula a subtração de dois números."""
    return x + (-y)

def multiplicacao(x, y):
    """Calcula o produto de dois números Inteiros."""
    total = 0
    for i in range(y):
        total += x
    return total

def divisao(x, y):
    """
    Calcula a divisão de dois números Inteiros.
    """
    if y == 0:
        return "Erro: Divisão por zero não é permitida."

    i = 0
    while y <= x:
        x -= y
        i += 1
        print(f"x: {x}")
        print(f"y: {y}")
        print(f"i: {i}")
        
    return f"{i} com resto {x}"
