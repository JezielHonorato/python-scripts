import os
import pdfplumber
from . import utils


def _converter_pdf_para_texto(
    caminho_pdf, caminho_destino, formato
):
    if not os.path.exists(caminho_pdf):
        print(f"Erro: o arquivo '{caminho_pdf}' não foi encontrado.")
        return

    texto_completo = ""
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto_completo += pagina.extract_text() + "\n"
    except Exception as e:
        print(f"Ocorreu um erro ao ler o PDF: {e}")
        return

    nome_base = os.path.splitext(os.path.basename(caminho_pdf))[0]
    nome_base_formatado = utils.formatar_nome(nome_base)
    nome_arquivo_saida = os.path.join(
        caminho_destino, f"{nome_base_formatado}.{formato}"
    )

    try:
        with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
            arquivo_saida.write(texto_completo)
        print(f"Sucesso! o texto foi salvo em '{nome_arquivo_saida}'")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo de saída: {e}")
        raise

def executar_conversao(caminho_origem, caminho_destino, formato="md"):
    total_convertidos = 0
    total_erros = 0
    
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino, exist_ok=True)

    if os.path.isfile(caminho_origem):
        if caminho_origem.lower().endswith(".pdf"):
            print(f"\nAnalisando arquivo: '{caminho_origem}'")
            try:
                _converter_pdf_para_texto(caminho_origem, caminho_destino, formato)
                total_convertidos += 1
            except Exception:
                total_erros += 1
        else:
            print(f"Erro: O arquivo selecionado '{os.path.basename(caminho_origem)}' não é um PDF.")
            total_erros += 1

    elif os.path.isdir(caminho_origem):
        for pasta, _, arquivos in os.walk(caminho_origem):
            for nome_arquivo in arquivos:
                if nome_arquivo.lower().endswith(".pdf"):
                    caminho_pdf = os.path.join(pasta, nome_arquivo)
                    print(f"\nAnalisando: '{caminho_pdf}'")
                    try:
                        _converter_pdf_para_texto(caminho_pdf, caminho_destino, formato)
                        total_convertidos += 1
                    except Exception:
                        total_erros += 1
    else:
        print(f"Erro: O caminho de origem '{caminho_origem}' não existe.")
        total_erros += 1


    print("\n--- Processamento Concluído ---")
    print(f"Total de PDFs convertidos com sucesso: {total_convertidos}")
    print(f"Total de erros: {total_erros}")