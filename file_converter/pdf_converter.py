import pdfplumber
from dotenv import load_dotenv
import os

load_dotenv()
ORIGEM = os.getenv("ORIGEM")
DESTINO = os.getenv("DESTINO")

def converter_pdf(caminho_origem, extensao = "txt"):
    if not os.path.exists(caminho_origem):
        print(f"Erro: o arquivo '{caminho_origem}' não foi encontrado.")
        return

    texto_completo = ""
    try:
        with pdfplumber.open(caminho_origem) as pdf:
            for pagina in pdf.pages:
                texto_completo += pagina.extract_text() + "\n"
    except Exception as e:
        print(f"Ocorreu um erro ao ler o PDF: {e}")
        return

    nome_base = os.path.splitext(os.path.basename(caminho_origem))[0]
    nome_arquivo_saida = os.path.join(DESTINO, f"{nome_base}.{extensao}")

    try:
        with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
            arquivo_saida.write(texto_completo)
        print(f"Sucesso! o texto foi salvo em '{nome_arquivo_saida}'")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo de saída: {e}")

converter_pdf(ORIGEM, DESTINO)
