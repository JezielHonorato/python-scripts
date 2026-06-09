import sqlite3
import json

from pathlib import Path

arquivo_origem = Path(r"C:\Nome do Caminho do arquivo.db")
arquivo_destino = Path(r"C:\Nome do Caminho do arquivo.json a ser criado")


def sqlite_to_json(db_file, json_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Obter todas as tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [table[0] for table in cursor.fetchall()]

    data = {}
    for table_name in tables:
        # Obter todas as colunas
        cursor.execute(f"PRAGMA table_info('{table_name}')")
        columns = [col[1] for col in cursor.fetchall()]

        # Obter todos os dados da tabela
        cursor.execute(f"SELECT * FROM '{table_name}'")
        rows = cursor.fetchall()

        # Converter dados para listas de dicionários
        table_data = []
        for row in rows:
            table_data.append(dict(zip(columns, row)))

        data[table_name] = table_data

    conn.close()

    # Escrever dados no arquivo JSON
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Banco de dados SQLite '{db_file}' convertido para '{json_file}'")


# Exemplo de uso:
sqlite_to_json(arquivo_origem, arquivo_destino)
