import os
import shutil

def organizarArquivos(pasta):
  pasta_organizada = os.path.join(os.getcwd(), pasta)

  for file in os.listdir(pasta_organizada):
    caminho_completo = os.path.join(pasta_organizada, file)
    if os.path.isfile(caminho_completo):
      nome, extensao = os.path.splitext(file)
      extensao = extensao[1:] or "sem_extensao"
      destino = os.path.join(pasta_organizada, extensao)

      if not os.path.isdir(destino):
        os.mkdir(destino)

      print(f'O arquivo "{file}" será movido para a pasta "{extensao}"')
      shutil.move(caminho_completo, os.path.join(destino, file))
    else:
      print(f'"{file}" é uma pasta, ignorando.')

organizarArquivos('downloads')
