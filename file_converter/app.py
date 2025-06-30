# app_gui.py

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import os

from conversores import conversor_pdf, conversor_img, conversor_font


class ConversorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Arquivos Universal")
        self.root.geometry("500x350")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", padding=6, relief="flat", background="#ccc")
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))
        self.style.configure("Header.TLabel", font=("Helvetica", 14, "bold"))

        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(expand=True, fill=tk.BOTH)

        header_label = ttk.Label(
            main_frame, text="Selecione o Tipo de Conversão", style="Header.TLabel"
        )
        header_label.pack(pady=(0, 20))

        btn_pdf_to_text = ttk.Button(
            main_frame, text="PDF para Texto (.md/.txt)", command=self.abrir_janela_pdf
        )
        btn_pdf_to_text.pack(fill=tk.X, pady=5)

        btn_img_to_pdf = ttk.Button(
            main_frame, text="Imagens para PDF", command=self.abrir_janela_img
        )
        btn_img_to_pdf.pack(fill=tk.X, pady=5)

        btn_font = ttk.Button(
            main_frame,
            text="Converter Fontes (TTF para Web)",
            command=self.abrir_janela_font,
        )
        btn_font.pack(fill=tk.X, pady=5)

        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(
            root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W, padding=5
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_var.set("Pronto")

    def abrir_janela_pdf(self):
        self.criar_janela_conversao(
            titulo="PDF para Texto",
            label_origem="Arquivo ou Pasta de Origem (PDFs):",
            funcao_conversao=conversor_pdf.executar_conversao,
            modo_selecao_origem="arquivo_ou_pasta",
            opcoes_extras=["formato"],
        )

    def abrir_janela_img(self):
        self.criar_janela_conversao(
            titulo="Imagens para PDF",
            label_origem="Pasta Raiz com Subpastas de Imagens:",
            funcao_conversao=conversor_img.executar_conversao,
            modo_selecao_origem="pasta_apenas",
        )

    def abrir_janela_font(self):
        self.criar_janela_conversao(
            titulo="Converter Fontes",
            label_origem="Arquivo ou Pasta de Origem (TTFs):",
            funcao_conversao=conversor_font.executar_conversao,
            modo_selecao_origem="arquivo_ou_pasta",
        )

    def criar_janela_conversao(
        self,
        titulo,
        label_origem,
        funcao_conversao,
        modo_selecao_origem,
        opcoes_extras=None,
    ):
        janela = tk.Toplevel(self.root)
        janela.title(titulo)
        janela.geometry("600x320")

        frame = ttk.Frame(janela, padding="15")
        frame.pack(expand=True, fill=tk.BOTH)

        origem_var = tk.StringVar()
        destino_var = tk.StringVar()

        ttk.Label(frame, text=label_origem).grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=2
        )
        entry_origem = ttk.Entry(frame, textvariable=origem_var)
        entry_origem.grid(row=1, column=0, columnspan=3, sticky=tk.EW)

        if modo_selecao_origem == "arquivo_ou_pasta":
            btn_origem_arq = ttk.Button(
                frame,
                text="Selecionar Arquivo...",
                command=lambda: self.selecionar_arquivo(origem_var),
            )
            btn_origem_arq.grid(row=2, column=0, sticky=tk.W, pady=5)
            btn_origem_pasta = ttk.Button(
                frame,
                text="Selecionar Pasta...",
                command=lambda: self.selecionar_pasta(origem_var),
            )
            btn_origem_pasta.grid(row=2, column=1, sticky=tk.W, pady=5)
        elif modo_selecao_origem == "pasta_apenas":
            btn_origem_pasta = ttk.Button(
                frame,
                text="Selecionar Pasta...",
                command=lambda: self.selecionar_pasta(origem_var),
            )
            btn_origem_pasta.grid(row=2, column=0, sticky=tk.W, pady=5)

        ttk.Label(frame, text="Pasta de Destino:").grid(
            row=3, column=0, columnspan=2, sticky=tk.W, pady=(10, 2)
        )
        entry_destino = ttk.Entry(frame, textvariable=destino_var)
        entry_destino.grid(row=4, column=0, columnspan=3, sticky=tk.EW)
        btn_destino = ttk.Button(
            frame,
            text="Selecionar Pasta...",
            command=lambda: self.selecionar_pasta(destino_var),
        )
        btn_destino.grid(row=5, column=0, sticky=tk.W, pady=5)

        frame.grid_columnconfigure(0, weight=1)

        opcoes_vars = {}
        row_seguinte = 6
        if opcoes_extras and "formato" in opcoes_extras:
            ttk.Label(frame, text="Formato de Saída:").grid(
                row=row_seguinte, column=0, sticky=tk.W, pady=(10, 2)
            )
            row_seguinte += 1
            formato_var = tk.StringVar(value="md")
            opcoes_vars["formato"] = formato_var
            combo_formato = ttk.Combobox(
                frame, textvariable=formato_var, values=["md", "txt"], state="readonly"
            )
            combo_formato.grid(row=row_seguinte, column=0, sticky=tk.W)
            row_seguinte += 1

        def run_conversion():
            origem = origem_var.get()
            destino = destino_var.get()
            if not origem or not destino:
                messagebox.showerror(
                    "Erro",
                    "A origem e o destino devem ser selecionados.",
                    parent=janela,
                )
                return

            kwargs = {"caminho_origem": origem, "caminho_destino": destino}
            if "formato" in opcoes_vars:
                kwargs["formato"] = opcoes_vars["formato"].get()

            threading.Thread(
                target=self.executar_em_thread,
                args=(funcao_conversao, kwargs, janela),
                daemon=True,
            ).start()

        btn_converter = ttk.Button(
            frame, text="Iniciar Conversão", command=run_conversion
        )
        btn_converter.grid(row=row_seguinte, column=0, columnspan=3, pady=(20, 0))

    def selecionar_arquivo(self, var_alvo):
        caminho_arquivo = filedialog.askopenfilename()
        if caminho_arquivo:
            var_alvo.set(caminho_arquivo)

    def selecionar_pasta(self, var_alvo):
        caminho_pasta = filedialog.askdirectory()
        if caminho_pasta:
            var_alvo.set(caminho_pasta)

    def executar_em_thread(self, funcao, kwargs, janela_ativa):
        self.status_var.set(
            f"Processando '{os.path.basename(kwargs['caminho_origem'])}'..."
        )
        try:
            funcao(**kwargs)
            self.status_var.set("Conversão concluída com sucesso!")
            messagebox.showinfo(
                "Sucesso", "A conversão foi concluída!", parent=janela_ativa
            )
        except Exception as e:
            self.status_var.set(f"Erro durante a conversão: {e}")
            messagebox.showerror(
                "Erro de Conversão", f"Ocorreu um erro:\n{e}", parent=janela_ativa
            )


if __name__ == "__main__":
    app_root = tk.Tk()
    app = ConversorApp(app_root)
    app_root.mainloop()
