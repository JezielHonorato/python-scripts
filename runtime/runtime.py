import subprocess
import time
import statistics
import os
from dotenv import load_dotenv

load_dotenv()
ORIGEM = os.getenv("ORIGEM")


def medir_tempo_medio(comando, num_execucoes=5):
    tempos = []
    print(f"Preparando para executar o comando: '{comando}' {num_execucoes} vezes...\n")

    for i in range(num_execucoes):
        start_time = time.time()
        try:
            process = subprocess.run(
                comando, shell=True, capture_output=True, text=True, check=True
            )
            end_time = time.time()
            duracao = end_time - start_time
            tempos.append(duracao)
            print(
                f"Execução {i+1}/{num_execucoes}: Concluída em {duracao:.4f} segundos"
            )

        except subprocess.CalledProcessError as e:
            print(f"Erro na execução {i+1}/{num_execucoes} do comando:")
            print(f"  Comando: {e.cmd}")
            print(f"  Código de Saída: {e.returncode}")
            print(f"  Saída Padrão (stdout): {e.stdout}")
            print(f"  Saída de Erro (stderr): {e.stderr}")
            print("Abortando medições devido ao erro.")
            return None, tempos, e.stdout, e.stderr
        except FileNotFoundError:
            print(f"Erro: O comando '{comando.split()[0]}' não foi encontrado.")
            print("Verifique se o programa está no PATH ou se o caminho está correto.")
            return None, tempos, "", "Comando não encontrado."
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None, tempos, "", str(e)

    if not tempos:
        print("Nenhuma execução foi bem-sucedida para calcular a média.")
        return None, [], "", ""

    media = statistics.mean(tempos)
    saida_final_stdout = process.stdout if "process" in locals() else ""
    saida_final_stderr = process.stderr if "process" in locals() else ""

    return media, saida_final_stdout, saida_final_stderr


numero_de_execucoes = 10

print("-" * 40)
print("Iniciando medição de tempo de execução...")
media_tempo, ultima_saida, ultimo_erro = medir_tempo_medio(ORIGEM, numero_de_execucoes)
print("-" * 40)

if media_tempo is not None:
    print(f"\nResultados para o comando: '{ORIGEM}'")
    print(f"Número de execuções: {numero_de_execucoes}")
    print(f"Tempo médio de execução: {media_tempo:.4f} segundos")

    if ultima_saida:
        print("\nÚltima Saída (stdout) do programa:")
        print(ultima_saida.strip())
    if ultimo_erro:
        print("\nÚltima Saída de Erro (stderr) do programa:")
        print(ultimo_erro.strip())
else:
    print("\nNão foi possível calcular a média devido a erros durante as execuções.")

print("\nMedição concluída.")
