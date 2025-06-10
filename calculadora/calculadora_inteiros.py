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

