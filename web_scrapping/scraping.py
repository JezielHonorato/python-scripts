import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

MATRICULA = os.getenv("MATRICULA")
SENHA = os.getenv("SENHA")

# Definir as opções do site
def acessarNotas(MATRICULA, SENHA):
  options = Options()
  options.add_argument('headless') # não aparecer
  options.add_argument('window-size=400,800')

  driver = webdriver.Chrome(options=options) 
  driver.get('https://suap.ifrn.edu.br') # Abrir o navegador

  print(driver.page_source)

  #Logar
  user = driver.find_element(By.ID, "id_username")
  user.send_keys(MATRICULA)

  senha = driver.find_element(By.ID, "id_password")
  senha.send_keys(SENHA)
  senha.submit()

  #Redirecionar para o boletim
  driver.get('https://suap.ifrn.edu.br/edu/aluno/20211144010003/?tab=boletim') 
  sleep(2)

  conteudo = driver.page_source

  site = BeautifulSoup(conteudo, 'html.parser')

  boletim = site.find('table', attrs={'class': 'borda'})
  materias = boletim.findAll('tr')

  lista_notas = []

  sleep(2)
  for materia in materias:
    nome = materia.css.select_one("td:nth-child(2)")
    nota1 = materia.css.select_one("td:nth-child(8)")
    nota2 = materia.css.select_one("td:nth-child(10)")
    nota3 = materia.css.select_one("td:nth-child(12)")
    nota4 = materia.css.select_one("td:nth-child(14)")
    media = materia.css.select_one("td:nth-child(19)")

    if nome is not None and nota1 is not None and nota2 is not None and nota3 is not None and nota4 is not None and media is not None:
      lista_notas.append([nome.text, nota1.text, nota2.text, nota3.text, nota4.text, media.text])
    else:
      print(f"Não foi possível encontrar os elementos na linha")


  planilha = pd.DataFrame(lista_notas, columns=['materia', 'nota 1', 'nota 2', 'nota 3', 'nota 4', 'media'])

  planilha.to_excel('notas.xlsx', index=False)

acessarNotas()