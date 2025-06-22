import os
from fontTools.ttLib import TTFont
from dotenv import load_dotenv

load_dotenv()
ORIGEM = os.getenv("ORIGEM")
DESTINO = os.getenv("DESTINO")


def converter_fonte(caminho_origem, caminho_destino):
    if not os.path.exists(caminho_origem):
        print(f"Erro: O arquivo '{caminho_origem}' não foi encontrado.")
        return

    nome_base = os.path.splitext(os.path.basename(caminho_origem))[0]
    caminho_woff = os.path.join(caminho_destino, f"{nome_base}.woff")
    caminho_woff2 = os.path.join(caminho_destino, f"{nome_base}.woff2")

    try:
        font = TTFont(caminho_origem)

        font.save(caminho_woff)
        print(f"Sucesso: Arquivo WOFF salvo em '{caminho_woff}'")

        font.save(caminho_woff2, flavors=["woff2"])
        print(f"Sucesso: Arquivo WOFF2 salvo em '{caminho_woff2}'")

    except Exception as e:
        print(f"Ocorreu um erro durante a conversão: {e}")


def pecorrer_pasta(caminho_origem, caminho_destino):
    total_convertidos = 0
    total_erros = 0

    for pasta, subpasta, arquivo in os.walk(caminho_origem):
        for nome_arquivo in arquivo:
            if nome_arquivo.lower().endswith(".ttf"):
                caminho_arquivo = os.path.join(pasta, nome_arquivo)
                print(f"\nAnalisando: '{caminho_arquivo}'")
                try:
                    converter_fonte(caminho_arquivo, caminho_destino)
                    total_convertidos += 1
                except Exception as e:
                    print(f"Erro inesperado ao processar '{caminho_arquivo}': {e}")
                    total_erros += 1

    return total_convertidos, total_erros


total_convertidos, total_erros = pecorrer_pasta(ORIGEM, DESTINO)
print("\n--- Processamento Concluído ---")
print(f"Total de Arquivos convertidos com sucesso: {total_convertidos}")
print(f"Total de erros/arquivos não processados: {total_erros}")
print(f"Os arquivos convertidos foram salvos em '{DESTINO}")
