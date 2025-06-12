# Operações matemticas

def soma(x, y):
    """Soma de dois números"""
    return x + y

def subtracao(x, y):
    """Subtração de dois números"""
    return x - y

def soma_neg(x, y):
    """Representação da subtração como soma de um número negativo"""
    return x + (-y)
    
def multiplicacao(x, y):
    """Produto de dois números"""
    return x * y

def multiplicacap_soma(x, y):
    """Representação da multiplicação como repetidas somas"""
    total = 0
    for i in range(y):
        total += x
        
    return total

def divisao(x, y):
    """Divisão de dois números"""
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def divisao_soma(x, y):
    """Divisão de dois números naturais"""
    if y == 0:
        return "Erro: Divisão por zero não é permitida."

    i = 0
    while y <= x:
        x -= y
        i += 1
        
    return f"{i} com resto {x}"

def potenciacao(x, y):
    """x elevado à y"""
    if x == 0 and y == 0:
        return "Erro: 0^0 é uma forma indeterminada."
    return x ** y

def potenciacao(x, y):
    """Representação da potenciação como repetidas multiplicações"""
    if x == 0 and y == 0:
        return "Erro: 0^0 é uma forma indeterminada."

    for i in range(y):
        for i in range(y):
            total += x
    return total

def radiciacao(x, y):
    """Raiz y-ésima de x (x elevado a 1/y)"""
    if y == 0:
        return "Erro: O índice da raiz não pode ser zero (não existe a 0ª raiz)."
    if x < 0 and y % 2 == 0:
        return "Erro: Raiz de número negativo com índice par não é um número real."
    return x ** (1 / y)

def raiz_quadrada(x):
    if x < 0:
        return "Erro: A raiz quadrada não pode ser negativa"
    
    i = 0
    while i <= x:
        if (multiplicacao(i, i) == x):
            return i

def equacao_linear(a, b):
    """Resolve uma equação de primeiro grau do tipo ax + b = 0"""
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
    
    delta = (b**2) - (4*a*c)

    if delta == 0:
        x = -b / (2*a)
        return f"Uma solução real (ou duas soluções iguais): x = {x:.4f}"
    elif delta > 0:
        delta = delta**(1/2)
        x1 = (-b + delta) / (2*a)
        x2 = (-b - delta) / (2*a)
        return f"Duas soluções reais: x1 = {x1:.4f} e x2 = {x2:.4f}"
    else:
        return "Nenhuma solução real (soluções são complexas)."
