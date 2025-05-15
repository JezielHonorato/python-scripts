import os
import shutil

def organizarArquivos(pasta):
  pasta_organizada = os.path.join(os.getcwd(), pasta)

  for file in os.listdir(pasta_organizada):
    conferir_arquivo = os.path.join(pasta_organizada, file)
    nome, extensao = os.path.splitext(file)
    extensao = extensao[1:]
    if os.path.isfile(conferir_arquivo):
      print(f'O arquivo {file} ser movido para pasta {extensao}')
    elif os.path.isdir(conferir_arquivo):
      print(f'Pasta: {nome}')
    
    pastas_geradas = f'{pasta_organizada}/{extensao}'
    
    if not os.path.isdir(pastas_geradas):
      os.mkdir(pastas_geradas)
    
    shutil.move(f'{pasta_organizada}/{file}', f'{pastas_geradas}/{file}')

organizarArquivos('downloads')