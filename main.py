import psutil
import time

while True:
    # Lista todos os processos em execução
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            process_name = proc.info['name']
            process_cmdline = proc.info['cmdline']
            pid = proc.info['pid']

            # Verifica se o processo é suspeito de ser um ransomware
            if 'ransom' in process_name.lower() or 'decrypt' in ' '.join(process_cmdline).lower():

                # Notifica o usuário sobre a atividade suspeita
                print(
                    f"Processo suspeito encontrado: {process_name} - {process_cmdline}")

                # Verifica se o processo está acessando um grande número de arquivos
                io_counters = proc.io_counters()
                if io_counters.read_count > 1000 or io_counters.write_count > 1000:
                    # Se o processo está acessando muitos arquivos, pode ser um ransomware criptografando os arquivos.
                    print(
                        f"Processo {process_name} pode estar criptografando arquivos.")
                else:
                    # Caso contrário, pode ser um falso positivo, então continue procurando.
                    continue

                # Encerra o processo malicioso
                proc.terminate()
                print(f"Processo {process_name} encerrado.")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Espera um tempo antes de verificar novamente
    time.sleep(5)
