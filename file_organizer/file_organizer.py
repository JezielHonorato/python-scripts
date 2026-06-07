import sys
import shutil
from pathlib import Path

caminho_da_pasta = Path(r"C:\Nome do Caminho da Pasta")


def organizar_arquivos(caminho_da_pasta):
    # .resolve() transforma qualquer caminho relativo em absoluto automaticamente.
    pasta = Path(caminho_da_pasta).resolve()

    if not pasta.is_dir():
        print(f"Erro: A pasta '{pasta}' não é válida ou não existe.")
        return

    print(f"Organizando arquivos em: {pasta}\n" + "-" * 30)

    for arquivo in pasta.iterdir():
        if arquivo.is_file():
            # .suffix pega a extensão com o ponto.
            extensao = arquivo.suffix[1:].lower() or "sem_extensao"
            pasta_destino = pasta / extensao
            pasta_destino.mkdir(exist_ok=True)
            arquivo_destino = pasta_destino / arquivo.name

            # Se o arquivo não existir no destino, move-o.
            if not arquivo_destino.exists():
                shutil.move(str(arquivo), str(pasta_destino))
                print(f'Movido: "{arquivo.name}" -> pasta "{extensao}"')
            else:
                print(f'Ignorado (já existe no destino): "{arquivo.name}"')


if __name__ == "__main__":
    # sys.argv é uma lista com as palavras digitadas no terminal;
    # sys.argv[0] é sempre o nome do seu script (script.py);
    # sys.argv[1] é o primeiro parâmetro passado depois do nome.

    if len(sys.argv) > 1:
        caminho_da_pasta = sys.argv[1]
    
    organizar_arquivos(caminho_da_pasta)
