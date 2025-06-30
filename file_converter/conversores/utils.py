import re
import unicodedata


def formatar_nome(nome):
    nome = nome.lower()
    nome = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode("utf-8")
    nome = re.sub(r"[^a-z0-9\s_-]", "", nome)
    nome = nome.replace(" ", "_")
    nome = nome.replace("_-", "-")
    nome = nome.replace("-_", "-")
    return nome
