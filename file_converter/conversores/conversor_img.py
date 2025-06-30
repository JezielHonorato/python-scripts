import os
from PIL import Image
from . import utils


def _converter_imagens_para_pdf(
    lista_imagens, caminho_saida_pdf
):  
    if not lista_imagens:
        print("Nenhuma imagem encontrada para conversão.")
        return

    try:
        imagens_abertas = []
        for caminho_imagem in lista_imagens:
            imagem = Image.open(caminho_imagem)
            imagens_abertas.append(imagem.convert("RGB"))

        primeira_imagem = imagens_abertas[0]
        imagens_restantes = imagens_abertas[1:]

        primeira_imagem.save(
            caminho_saida_pdf, save_all=True, append_images=imagens_restantes
        )
        print(f"Sucesso! PDF salvo em '{caminho_saida_pdf}'")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o PDF '{caminho_saida_pdf}': {e}")
        raise


def executar_conversao(caminho_origem, caminho_destino):
    total_convertidos = 0
    total_erros = 0
    extensoes_permitidas = [".png", ".jpg", ".jpeg"]

    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)

    for pasta_atual, _, arquivos in os.walk(caminho_origem):
        lista_de_arquivos_imagem = []
        for nome_arquivo in sorted(arquivos):
            if any(nome_arquivo.lower().endswith(ext) for ext in extensoes_permitidas):
                caminho_completo = os.path.join(pasta_atual, nome_arquivo)
                lista_de_arquivos_imagem.append(caminho_completo)

        if lista_de_arquivos_imagem:
            nome_da_pasta = os.path.basename(pasta_atual)
            nome_pdf_formatado = utils.formatar_nome(nome_da_pasta) + ".pdf"
            caminho_saida_pdf = os.path.join(caminho_destino, nome_pdf_formatado)

            print(f"\nAnalisando pasta: '{pasta_atual}'")
            print(f"Encontradas {len(lista_de_arquivos_imagem)} imagens.")

            try:
                _converter_imagens_para_pdf(lista_de_arquivos_imagem, caminho_saida_pdf)
                total_convertidos += 1
            except Exception:
                total_erros += 1

    print("\n--- Processamento Concluído ---")
    print(f"Total de pastas de imagens convertidas: {total_convertidos}")
    print(f"Total de erros: {total_erros}")
