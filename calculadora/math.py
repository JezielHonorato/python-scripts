# Todas as operações matemticas são somas.

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x + (-y)

def multiplicacao(x, y):
    total = 0

    for i in range(y):
        total += x
        
    return total

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."

    i = 0
    while y <= x:
        x -= y
        i += 1
        
    return f"{i} com resto {x}"

def potenciacao(x, y):
    if x == 0 and y == 0:
        return "Erro: 0^0 é uma forma indeterminada."

    for i in range(y):
        for i in range(y):
            total += x
    return total

def raiz_quadrada(x):
    if x < 0:
        return "Erro: A raiz quadrada não pode ser negativa"
    
    i = 0
    while i <= x:
        if (multiplicacao(i, i) == x):
            return i
