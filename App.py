import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import wmi
from Process import Process
import hashlib


# Checkbox checked
def check_one_checked():
    if checkbox1_state.get() == 1:
        checkbox2.deselect()


def check_two_checked():
    if checkbox2_state.get() == 1:
        checkbox1.deselect()


# Mapeando processos
def mapping_processes():
    for processo in processos:
        try:
            new_process = Process(
                processo.name(), processo.pid, processo.status())
            processos_lista.append(new_process)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


# Alertas
def show_help():
    messagebox.showinfo("Manual", "Modos de execução:\n\n - Modo de verificação: este modo é responsável por analisar o próximo processo que for executado na máquina e determinar se ele é um possível malware.\n - Modo constante: este modo é responsável por verificar todos os processos que forem executados na máquina e determinar se eles podem ser possíveis malwares.\n\nComo usar:\n\n1. Selecione a caixa correspondente ao modo de execução desejado.\n2. Clique em 'Iniciar execução'.")


def on_new_process_created(process):
    print(f"\033[36m| Novo processo encontrado: {process.Name}")


# Técnicas de analise
def verificar_hash_processo(process, lista_hashes_conhecidos):
    try:
        processid = psutil.Process(process.ProcessId)
        estado_processo = processid.as_dict(attrs=['memory_info'])

        # Calcular o hash do estado do processo
        hash_objeto = hashlib.sha256(str(estado_processo).encode())
        hash_calculado = hash_objeto.hexdigest()

        # Comparar o hash calculado com a lista de hashes conhecidos
        if hash_calculado in lista_hashes_conhecidos:
            # status id 2
            print(
                f"\033[36m| O hash do processo {process.Name} é conhecido. [PERIGOSO]")
        else:
            # status id 0
            print(
                f"\033[36m| O hash do processo {process.Name} não é conhecido.[SEGURO]")
    except psutil.NoSuchProcess:
        # status id 1
        print(f"\033[36m| Processo {process.Name} não encontrado.")
    except psutil.AccessDenied:
        # status id 1
        print(
            f'f"\033[36m| Permissão negada para encerrar o processo {process.Name}.')
    except IndexError:
        # status id 1
        print(f"\033[36m| Processo {process.Name} não encontrado.")
    except wmi.x_wmi:
        # status id 1
        print(
            f'f"\033[36m| Permissão negada para encerrar o processo {process.Name}.')


def verificar_instancia_processo(process):
    try:
        processid = psutil.Process(process.ProcessId)

        if int(process.ReadOperationCount) > 50:
            if int(process.WriteOperationCount) > 10:
                if process.PageFaults > 1000:
                    if process.ThreadCount > 5:
                        if process.HandleCount > 200:
                            processid.terminate()
                            # status id 2
                            print(f"\033[36m| [PERIGOSO] {process.Name}")
                        else:
                            # status id 1
                            print(f"\033[36m| [SUSPEITO] {process.Name}")
                    else:
                        # status id 1
                        print(f"\033[36m| [SUSPEITO] {process.Name}")
                else:
                    # status id 1
                    print(f"\033[36m| [SUSPEITO] {process.Name}")
            else:
                print(f"\033[36m| [SUSPEITO] {process.Name}")  # status id 1
        elif process.CommandLine == '"C:\Program Files\Malware\malware.exe" --payload':
            processid.terminate()
            print(f"\033[36m| {process.Name} [PERIGOSO]")  # status id 2
        elif process.KernelModeTime == "00:03:25":
            print(f"\033[36m| [SUSPEITO] {process.Name}")  # status id 1
        else:
            print(f"\033[36m| [SEGURO] {process.Name}")  # status id 0
    except psutil.NoSuchProcess:
        # status id 1
        print(f"\033[36m| [SUSPEITO] Processo {process.Name} não encontrado.")
    except psutil.AccessDenied:
        # status id 1
        print(
            f'f"\033[36m| [SUSPEITO] Permissão negada para encerrar o processo {process.Name}.')
    except IndexError:
        # status id 1
        print(f"\033[36m| [SUSPEITO] Processo {process.Name} não encontrado.")
    except wmi.x_wmi:
        # status id 1
        print(
            f'f"\033[36m| [SUSPEITO] Permissão negada para encerrar o processo {process.Name}.')

# Modos de execução


def verify_mode():
    print("\033[32m| Modo de verificação: LIGADO")
    try:
        wmi_service = wmi.WMI()
        watcher = wmi_service.Win32_Process.watch_for("creation")
        while checkbox1_state.get() == 1:
            process = watcher()
            on_new_process_created(process)
            # iniciar analise
            verificar_hash_processo(process, lista_hashs)
            verificar_instancia_processo(process)
            checkbox1.deselect()
            print("\033[31m| Modo de verificação: DESLIGADO")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")


def constant_mode():
    print("\033[32mModo constante: LIGADO")
    print("\033[31mModo constante: DESLIGADO")


# Tratando as opções do usuário
def start_exe():
    if checkbox1_state.get() == checkbox2_state.get():
        messagebox.showwarning(
            "Aviso", "Selecione um modo de execução para iniciar")
        return

    if checkbox1_state.get() == 1:
        verify_mode()
    else:
        constant_mode()


lista_hashs = ['hash1', 'hash2', 'hash3']
processos_lista = []
processos = psutil.process_iter()
mapping_processes()

root = tk.Tk()
icon = "img/aegis.ico"
root.iconbitmap(icon)
root.title("Aegis Defender")
root.geometry("400x200")
menubar = tk.Menu(root)
menu_principal = tk.Menu(menubar, tearoff=0)
menu_principal.add_command(label="Ajuda", command=show_help)
menu_principal.add_command(label="Sair", command=exit)
menubar.add_cascade(label="Configurações", menu=menu_principal)
root.config(menu=menubar)

checkbox1_state = tk.BooleanVar()
checkbox2_state = tk.BooleanVar()

label_frame = tk.LabelFrame(
    root, text="Modos de execução:", font=("Arial", 12))
label_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label = tk.Label(label_frame, text="Modo de verificação")
label.grid(row=0, column=0, padx=6, pady=6)

checkbox1 = tk.Checkbutton(label_frame, text="Marcar",
                           variable=checkbox1_state, command=check_one_checked)
checkbox1.grid(row=0, column=1, padx=5, pady=5)

label = tk.Label(label_frame, text="Modo constante")
label.grid(row=1, column=0, padx=6, pady=6)

checkbox2 = tk.Checkbutton(label_frame, text="Marcar",
                           variable=checkbox2_state, command=check_two_checked)
checkbox2.grid(row=1, column=1, padx=5, pady=5)

button = ttk.Button(
    root, text="Iniciar execução", command=start_exe)
button.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
