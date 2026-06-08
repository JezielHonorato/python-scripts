import sys
from pathlib import Path

pasta = Path(r"C:\Nome do Caminho da Pasta")


def file_tree(pasta, prefixo: str = ""):
    conteudos = []

    for p in pasta.iterdir():
        if not p.name.startswith("."):
            conteudos.append(p)

    # Forma compactada:
    # conteudos = [p for p in pasta.iterdir() if not p.name.startswith(".")]

    for i, item in enumerate(conteudos):
        ultimo_item = i == (len(conteudos) - 1)

        conector = "└── " if ultimo_item else "├── "

        print(f"{prefixo}{conector}{item.name}")
        if item.is_dir():
            file_tree(item, prefixo + ("    " if ultimo_item else "│   "))


if __name__ == "__main__":
    # sys.argv é uma lista com as palavras digitadas no terminal;
    # sys.argv[0] é sempre o nome do seu script (script.py);
    # sys.argv[1] é o primeiro parâmetro passado depois do nome.

    if len(sys.argv) > 1:
        caminho_da_pasta = sys.argv[1]
        pasta = Path(caminho_da_pasta).resolve()

        if not pasta.is_dir():
            print(f"Erro: A pasta '{pasta}' não é válida ou não existe.")
            sys.exit(1)

    print(f". {pasta}")
    file_tree(pasta)
