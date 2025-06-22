import pdfplumber
from dotenv import load_dotenv
import os
import re
import unicodedata

load_dotenv()
ORIGEM = os.getenv("ORIGEM")
DESTINO = os.getenv("DESTINO")


def formatar_nome(nome):
    # Modos de foramtação variam de acordo com o tipo de arquivo que será convertido
    nome = nome.lower()
    nome = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode("utf-8")
    nome = re.sub(r"[^a-z0-9\s_-]", "", nome)
    nome = nome.replace(" ", "_")
    nome = nome.replace("_-", "-")
    nome = nome.replace("-_", "-")

    return nome


def converter_pdf(caminho_pdf, caminho_destino, formato):
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
    nome_base_formatado = formatar_nome(nome_base)
    nome_arquivo_saida = os.path.join(
        caminho_destino, f"{nome_base_formatado}.{formato}"
    )

    try:
        with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
            arquivo_saida.write(texto_completo)
        print(f"Sucesso! o texto foi salvo em '{nome_arquivo_saida}'")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo de saída: {e}")


def pecorrer_pasta(caminho_origem, caminho_destino, formato="md"):
    # o formato pode ser .md ou .txt
    total_convertidos = 0
    total_erros = 0

    for pasta, subpasta, arquivo in os.walk(caminho_origem):
        for nome_arquivo in arquivo:
            if nome_arquivo.lower().endswith(".pdf"):
                caminho_pdf = os.path.join(pasta, nome_arquivo)
                print(f"\nAnalisando: '{caminho_pdf}'")
                try:
                    converter_pdf(caminho_pdf, caminho_destino, formato)
                    total_convertidos += 1
                except Exception as e:
                    print(f"Erro inesperado ao processar '{caminho_pdf}': {e}")
                    total_erros += 1

    return total_convertidos, total_erros


total_convertidos, total_erros = pecorrer_pasta(ORIGEM, DESTINO)
print("\n--- Processamento Concluído ---")
print(f"Total de PDFs convertidos com sucesso: {total_convertidos}")
print(f"Total de erros/arquivos não processados: {total_erros}")
print(f"Os arquivos convertidos foram salvos em '{DESTINO}")
