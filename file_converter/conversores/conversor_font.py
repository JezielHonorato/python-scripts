import os
from fontTools.ttLib import TTFont


def _converter_fonte_para_web(
    caminho_origem, caminho_destino
):
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
        raise


def executar_conversao(caminho_origem, caminho_destino):
    total_convertidos = 0
    total_erros = 0

    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino, exist_ok=True)

    if os.path.isfile(caminho_origem):
        if caminho_origem.lower().endswith(".ttf"):
            print(f"\nAnalisando arquivo: '{caminho_origem}'")
            try:
                _converter_fonte_para_web(caminho_origem, caminho_destino)
                total_convertidos += 1
            except Exception:
                total_erros += 1
        else:
            print(f"Erro: O arquivo selecionado '{os.path.basename(caminho_origem)}' não é um arquivo .ttf.")
            total_erros += 1

    elif os.path.isdir(caminho_origem):
        for pasta, _, arquivos in os.walk(caminho_origem):
            for nome_arquivo in arquivos:
                if nome_arquivo.lower().endswith(".ttf"):
                    caminho_arquivo = os.path.join(pasta, nome_arquivo)
                    print(f"\nAnalisando: '{caminho_arquivo}'")
                    try:
                        _converter_fonte_para_web(caminho_arquivo, caminho_destino)
                        total_convertidos += 1
                    except Exception:
                        total_erros += 1
    else:
        print(f"Erro: O caminho de origem '{caminho_origem}' não existe.")
        total_erros += 1


    print("\n--- Processamento Concluído ---")
    print(f"Total de fontes convertidas com sucesso: {total_convertidos}")
    print(f"Total de erros: {total_erros}")