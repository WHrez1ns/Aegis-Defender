import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import wmi
from Process import Process
from sklearn import tree


def check_one_checked():
    if checkbox1_state.get() == 1:
        checkbox2.deselect()


def check_two_checked():
    if checkbox2_state.get() == 1:
        checkbox1.deselect()


def mapping_processes():
    processos = psutil.process_iter()
    for processo in processos:
        try:
            new_process = Process(
                processo.name(), processo.pid)
            processos_lista.append(new_process)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def show_help():
    messagebox.showinfo("Manual", "Modos de execução:\n\n - Modo de verificação: este modo é responsável por analisar o próximo processo que for executado na máquina e determinar se ele é um possível malware.\n - Modo constante: este modo é responsável por verificar todos os processos que forem executados na máquina e determinar se eles podem ser possíveis malwares.\n\nComo usar:\n\n1. Selecione a caixa correspondente ao modo de execução desejado.\n2. Clique em 'Iniciar execução'.")


def show_exit():
    exit()


def on_new_process_created(process):
    print(f"\033[38m===================================================")
    print(f"\033[35m| Novo processo encontrado: {process.Name}")


def verificar_instancia_processo(process):
    checks = {
        "ReadOperationCount": (int(process.ReadOperationCount), 30),
        "WriteOperationCount": (int(process.WriteOperationCount), 300),
        "PageFaults": (process.PageFaults, 1000),
        "ThreadCount": (process.ThreadCount, 3),
        "HandleCount": (process.HandleCount, 60),
        "KernelModeTime": (process.KernelModeTime, "00:03:25")
    }

    status_list = []

    try:
        processid = psutil.Process(process.ProcessId)

        # verifica instancia
        for key, (value, threshold) in checks.items():
            if value >= threshold:
                print(f"\033[33m| [SUSPEITO] {key} > {threshold}: {value}")
                status_list.append(1)
            else:
                print(f"\033[33m| [SEGURO] {key} < {threshold}: {value}")
                status_list.append(0)
        print(f"\033[34m| [VERIFICAÇÃO] Status list: {status_list}")
        status_id = classif.predict([status_list])
        if status_id == 0:
            new_process = Process(
                process.Name, process.ProcessId)
            processos_lista.append(new_process)
            print(f"\033[32m| [SEGURO] Status id: 0 | {process.Name}")
        elif status_id == 1:
            resposta = messagebox.askquestion("Alerta", f"O processo {process.Name} possui um comportamento suspeito e pode danificar seu computador. Deseja encerrá-lo? No caso do programa ser desconhecido, recomenda-se o encerramento do mesmo.")
            if resposta == "sim" or resposta == "yes":
                processid.terminate()
                print(f"\033[33m| [SUSPEITO] Status id: 1 | {process.Name}")
            else:
                new_process = Process(
                    process.Name, process.ProcessId)
                processos_lista.append(new_process)
                print(f"\033[32m| [SEGURO] Status id: 0 | {process.Name}")
        else:
            processid.terminate()
            print(f"\033[31m| [PERIGOSO] Status id: 2 | {process.Name}")
    except psutil.NoSuchProcess:
        print(f"\033[33m| [SUSPEITO] Processo {process.Name} não encontrado")
    except psutil.AccessDenied:
        print(
            f'f"\033[33m| [SUSPEITO] Permissão negada para encerrar o processo {process.Name}')
    except IndexError:
        print(f"\033[33m| [SUSPEITO] Processo {process.Name} não encontrado")
    except wmi.x_wmi:
        print(
            f'f"\033[33m| [SUSPEITO] Permissão negada para encerrar o processo {process.Name}')


def analyse(process):
    for objeto in processos_lista:
        if objeto.nome == process.Name:
            return print(f"\033[32m| [SEGURO] Processo {process.Name} conhecido")
    print(f"\033[33m| [SUSPEITO] Processo {process.Name} desconhecido")
    verificar_instancia_processo(process)

def verify_mode():
    print("\033[36m| Modo de verificação: LIGADO")
    try:
        wmi_service = wmi.WMI()
        watcher = wmi_service.Win32_Process.watch_for("creation")
        while checkbox1_state.get() == 1:
            process = watcher()
            on_new_process_created(process)
            analyse(process)
            checkbox1.deselect()
            print("\033[31m| Modo de verificação: DESLIGADO")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")


def constant_mode():
    print("\033[36m| Modo constante: LIGADO")
    try:
        wmi_service = wmi.WMI()
        watcher = wmi_service.Win32_Process.watch_for("creation")
        while checkbox2_state.get() == 1:
            process = watcher()
            on_new_process_created(process)
            analyse(process)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")


def start_exe():
    if checkbox1_state.get() == checkbox2_state.get():
        messagebox.showwarning(
            "Aviso", "Selecione um modo de execução para iniciar")
        return
    if checkbox1_state.get() == 1:
        verify_mode()
    else:
        constant_mode()


def main():
    global features
    features = [
        # 20 features
        [0, 0, 0, 0, 0, 0],  # status id = 0
        [1, 0, 0, 0, 0, 0],  # status id = 0
        [1, 1, 0, 0, 0, 0],  # status id = 0
        [1, 1, 1, 0, 0, 0],  # status id = 0
        [0, 0, 0, 1, 0, 0],  # status id = 0
        [0, 0, 0, 1, 1, 0],  # status id = 0
        [0, 0, 0, 1, 1, 1],  # status id = 0
        [1, 0, 1, 0, 0, 0],  # status id = 0
        [1, 0, 1, 1, 0, 0],  # status id = 0
        [0, 1, 0, 1, 0, 0],  # status id = 0
        [0, 1, 0, 1, 1, 0],  # status id = 0
        [0, 0, 1, 0, 1, 0],  # status id = 0
        [0, 0, 1, 0, 1, 1],  # status id = 0
        [0, 1, 0, 1, 0, 1],  # status id = 0
        [1, 0, 1, 0, 1, 0],  # status id = 0
        [1, 1, 0, 1, 0, 0],  # status id = 0
        [1, 1, 0, 0, 1, 0],  # status id = 0
        [1, 1, 0, 0, 0, 1],  # status id = 0
        [0, 1, 1, 0, 0, 1],  # status id = 0
        [0, 0, 1, 1, 0, 1],  # status id = 0

        # 15 features
        [1, 1, 1, 1, 0, 0],  # status id = 1
        [0, 1, 1, 1, 1, 0],  # status id = 1
        [0, 0, 1, 1, 1, 1],  # status id = 1
        [1, 0, 1, 1, 1, 0],  # status id = 1
        [1, 0, 0, 1, 1, 1],  # status id = 1
        [1, 1, 0, 1, 1, 0],  # status id = 1
        [1, 1, 0, 0, 1, 1],  # status id = 1
        [0, 1, 1, 1, 1, 0],  # status id = 1
        [0, 1, 1, 0, 1, 1],  # status id = 1
        [0, 1, 0, 1, 1, 1],  # status id = 1
        [1, 0, 1, 1, 1, 1],  # status id = 1
        [1, 1, 0, 1, 1, 1],  # status id = 1
        [1, 1, 1, 0, 1, 1],  # status id = 1
        [1, 1, 1, 1, 0, 1],  # status id = 1
        [1, 0, 0, 1, 1, 0],  # status id = 1

        # 2 feature
        [0, 1, 1, 1, 1, 1],  # status id = 2
        [1, 1, 1, 1, 1, 1],  # status id = 2
    ]

    global labels
    labels = [
        # 20 labels
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

        # 15 labels
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

        # 2 label
        2, 2
    ]

    global classif
    classif = tree.DecisionTreeClassifier()
    classif.fit(features, labels)

    global processos_lista
    processos_lista = []
    mapping_processes()

    root = tk.Tk()
    # icon = "aegis.ico"
    # root.iconbitmap(icon)
    root.title("Aegis Defender")
    root.geometry("400x200")
    menubar = tk.Menu(root)
    menu_principal = tk.Menu(menubar, tearoff=0)
    menu_principal.add_command(label="Ajuda", command=show_help)
    menu_principal.add_command(label="Sair", command=show_exit)
    menubar.add_cascade(label="Configurações", menu=menu_principal)
    root.config(menu=menubar)

    global checkbox1_state
    checkbox1_state = tk.BooleanVar()
    global checkbox2_state
    checkbox2_state = tk.BooleanVar()

    label_frame = tk.LabelFrame(
        root, text="Modos de execução:", font=("Arial", 12))
    label_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    '''label = tk.Label(label_frame, text="Modo de verificação")
    label.grid(row=0, column=0, padx=6, pady=6)'''

    global checkbox1
    checkbox1 = tk.Checkbutton(label_frame,
                               text="Marcar",
                               variable=checkbox1_state,
                               command=check_one_checked)
    # checkbox1.grid(row=0, column=1, padx=5, pady=5)

    label = tk.Label(label_frame, text="Modo constante")
    label.grid(row=1, column=0, padx=6, pady=6)

    global checkbox2
    checkbox2 = tk.Checkbutton(label_frame,
                               text="Marcar",
                               variable=checkbox2_state,
                               command=check_two_checked)
    checkbox2.grid(row=1, column=1, padx=5, pady=5)

    button = ttk.Button(
        root, text="Iniciar execução", command=start_exe)
    button.grid(row=2, column=0, padx=10, pady=10)

    root.mainloop()