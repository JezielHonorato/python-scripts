import tkinter as tk
from tkinter import messagebox

# Funções matemáticas
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

# Função de cálculo
def calcular(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos")
        return

    match op:
        case 'soma': result = soma(a, b)
        case 'sub': result = subtracao(a, b)
        case 'mult': result = multiplicacao(a, b)
        case 'div': result = divisao(a, b)
        case 'pot': result = potenciacao(a, b)
        case 'rad': result = radiciacao(a, b)

    resultado_var.set(f"Resultado: {result}")

# Interface gráfica
janela = tk.Tk()
janela.title("Calculadora Bonita")
janela.configure(bg="#f0f4f8")
janela.geometry("300x420")
janela.resizable(False, False)

estilo_entry = {'font': ('Arial', 14), 'bg': '#ffffff', 'bd': 2, 'relief': 'groove'}
estilo_label = {'font': ('Arial', 12), 'bg': '#f0f4f8'}
estilo_botao = {'font': ('Arial', 12), 'bg': '#4a90e2', 'fg': 'white', 'activebackground': '#357ab8', 'bd': 0}

# Entradas
tk.Label(janela, text="Número A:", **estilo_label).pack(pady=(20, 0))
entry1 = tk.Entry(janela, **estilo_entry, justify='center')
entry1.pack(pady=5, ipady=4)

tk.Label(janela, text="Número B:", **estilo_label).pack(pady=(10, 0))
entry2 = tk.Entry(janela, **estilo_entry, justify='center')
entry2.pack(pady=5, ipady=4)

# Botões
frame_botoes = tk.Frame(janela, bg="#f0f4f8")
frame_botoes.pack(pady=15)

botoes = [
    ("Soma (+)", 'soma'),
    ("Subtração (-)", 'sub'),
    ("Multiplicação (×)", 'mult'),
    ("Divisão (÷)", 'div'),
    ("Potenciação (^)", 'pot'),
    ("Radiciação (^(1/B))", 'rad')
]

for texto, op in botoes:
    tk.Button(frame_botoes, text=texto, command=lambda op=op: calcular(op), **estilo_botao).pack(fill='x', padx=20, pady=4, ipady=4)

# Resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(janela, textvariable=resultado_var, font=('Arial', 14, 'bold'), bg="#f0f4f8", fg="#333")
resultado_label.pack(pady=20)

janela.mainloop()
