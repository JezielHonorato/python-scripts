from pathlib import Path

pasta = Path(r"C:\Nome do Caminho da Pasta")  # Caminho para a pasta

# for arquivo in pasta.iterdir():   # para cada arquivo na pasta
# for arquivo in pasta.glob():      # para adcionar padrões na pesquisa
# for arquivo in pasta.rglob():     # para cada arquivo na pasta e em todas as subpastas
for arquivo in pasta.rglob("*"):
    if arquivo.is_file():
        novo_nome = arquivo.name.replace(" Avalos", "")
        novo_caminho = arquivo.with_name(novo_nome)

        arquivo.rename(novo_caminho)

        print(f"{arquivo.name} -> {novo_nome}")
