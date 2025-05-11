import requests
from dotenv import load_dotenv
import os

load_dotenv() #Variaveis salvas em .env ignorado.
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("USERNAME")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def listar_repositorios():
    repos = []
    page = 1 # Divisao em paginas para quem possui mais de 30 repositorios
    while True:
        url = f"https://api.github.com/user/repos?per_page=30&page={page}"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Erro ao listar repositórios: {response.status_code}")
            break
        
        data = response.json()
        if not data:  
            break
        
        repos.extend(data)
        page += 1 

    return repos

def deletar_repositorios(repos):
    for repo in repos:
        nome = repo["name"]
        full_name = repo["full_name"]
        url_delete = f"https://api.github.com/repos/{full_name}"
        response = requests.delete(url_delete, headers=headers)
        
        if response.status_code == 204:
            print(f"Repositório excluído: {nome}")
        else:
            print(f"Falha ao excluir: {nome} - Código {response.status_code}")

if __name__ == "__main__":
    repos = listar_repositorios()
    
    if not repos:
        print("Nenhum repositório encontrado.")
    else:
        print(f"{len(repos)} repositórios encontrados.")
        confirm = input("Tem certeza que deseja excluir todos? (y/n): ")
        
        if confirm.lower() == "y":
            deletar_repositorios(repos)
        else:
            print("Cancelado.")
