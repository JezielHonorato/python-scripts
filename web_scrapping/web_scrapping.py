import logging
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def acessarNotas(matricula, senha):
    options = Options()
    options.add_argument('headless')
    options.add_argument('window-size=400,800')

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get('https://suap.ifrn.edu.br')

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_username")))
        user = driver.find_element(By.ID, "id_username")
        user.send_keys(matricula)

        senha = driver.find_element(By.ID, "id_password")
        senha.send_keys(senha)
        senha.submit()

        WebDriverWait(driver, 10).until(EC.url_contains('/edu/aluno'))
        driver.get(f"https://suap.ifrn.edu.br/edu/aluno/{matricula}/?tab=boletim")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "borda")))

        conteudo = driver.page_source
        boletim = BeautifulSoup(conteudo, 'html.parser').find('table', attrs={'class': 'borda'})
        materias = boletim.findAll('tr')

        lista_notas = []
        
        for materia in materias:
            try:
                nome = materia.select_one("td:nth-child(2)")
                nota1 = materia.select_one("td:nth-child(8)")
                nota2 = materia.select_one("td:nth-child(10)")
                nota3 = materia.select_one("td:nth-child(12)")
                nota4 = materia.select_one("td:nth-child(14)")
                media = materia.select_one("td:nth-child(19)")

                if all([nome, nota1, nota2, nota3, nota4, media]):
                    lista_notas.append([nome.text.strip(), nota1.text.strip(), nota2.text.strip(), nota3.text.strip(), nota4.text.strip(), media.text.strip()])
                else:
                    logging.warning("Não foi possível encontrar os dados de uma matéria.")
            except Exception as e:
                logging.error(f"Erro ao processar matéria: {e}")

        planilha = pd.DataFrame(lista_notas, columns=['Materia', 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Média'])
        planilha.to_excel('notas.xlsx', index=False)
        logging.info("Notas salvas com sucesso.")

    except Exception as e:
        logging.error(f"Erro ao acessar o site ou processar dados: {e}")
    finally:
        driver.quit()

logging.basicConfig(level=logging.INFO)

acessarNotas('matricula_test', 'password_test')
