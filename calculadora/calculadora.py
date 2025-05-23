import tkinter as tk
from tkinter import messagebox

def soma(x, y): return x + y
def subtracao(x, y): return x - y
def multiplicacao(x, y): return x * y
def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y
def potenciacao(x, y): return x ** y
def radiciacao(x, y):
    if y == 0:
        return "Erro: Radiciação com expoente zero"
    return x ** (1 / y)

def calcular(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos")
        return

    match op:
        case 'soma': result = soma(a, b)
        case 'subtracao': result = subtracao(a, b)
        case 'multiplicacao': result = multiplicacao(a, b)
        case 'divisao': result = divisao(a, b)
        case 'potenciacao': result = potenciacao(a, b)
        case 'radiciacao': result = radiciacao(a, b)

    resultado_var.set(f"Resultado: {result}")

# Interface gráfica
janela = tk.Tk()
janela.title("Calculadora")

tk.Label(janela, text="Número A:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(janela)
entry1.grid(row=0, column=1)

tk.Label(janela, text="Número B:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(janela)
entry2.grid(row=1, column=1)

# Botões das operações
botoes = [
    ("Soma (+)", 'soma'),
    ("Subtração (-)", 'subtracao'),
    ("Multiplicação (×)", 'multiplicacao'),
    ("Divisão (÷)", 'divisao'),
    ("Potenciação (^)", 'potenciacao'),
    ("Radiciação (^(1/B))", 'radiciacao')
]

for i, (texto, op) in enumerate(botoes, start=2):
    tk.Button(janela, text=texto, width=20, command=lambda op=op: calcular(op)).grid(row=i, column=0, columnspan=2, pady=2)

resultado_var = tk.StringVar()
tk.Label(janela, textvariable=resultado_var, font=('Arial', 12, 'bold')).grid(row=8, column=0, columnspan=2, pady=10)

janela.mainloop()
