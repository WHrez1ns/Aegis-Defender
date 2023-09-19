import os
import ctypes
import sys
from tkinter import messagebox
import psutil
import wmi
from sklearn import tree
import json
import webview


def show_help():
        messagebox.showinfo("Manual", "Modos de execução:\n\n - Modo constante: este modo é responsável por verificar todos os processos que forem executados na máquina e determinar se eles podem ser possíveis ameaças.\n\nComo usar:\n\n1. Selecione a caixa correspondente ao modo de execução desejado.\n2. Clique em 'Iniciar execução'.")


def show_exit():
    exit()


def new_item_in_json(json_file, name, sid):
    with open(json_file, 'r') as file:
        data = json.load(file)
        index = len(data)

    new_item = {
        "name":name,
        "index":index,
        "sid":sid
    }

    data.append(new_item)

    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)


def on_new_process_created(process):
    print(f"\033[38m===================================================")
    print(f"\033[35m| Novo processo encontrado: {process.Name}")


def instance_analysis(process):
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

        for key, (value, threshold) in checks.items():
            if value >= threshold:
                print(f"\033[33m| [SUSPEITO] {key} >= {threshold}: {value}")
                status_list.append(1)
            else:
                print(f"\033[33m| [SEGURO] {key} < {threshold}: {value}")
                status_list.append(0)
        print(f"\033[34m| [VERIFICAÇÃO] Status list: {status_list}")
        status_id = classif.predict([status_list])
        if status_id == 2:
            processid.terminate()
            print(f"\033[31m| [PERIGOSO] Ameaça neutralizada: {process.Name} | Status id: 2")
            new_item_in_json("process.json", process.Name, 2)
        elif status_id == 1:
            processid.terminate()
            print(f"\033[31m| [SUSPEITO] Processo possui um comportamento suspeito: {process.Name} | Status id: 1")
            new_item_in_json("process.json", process.Name, 2)
        else:
            print(f"\033[32m| [SEGURO] Status id: 0 | {process.Name}")
            new_item_in_json("process.json", process.Name, 0)
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
    with open("static/json/process.json", 'r') as file:
        data = json.load(file)
        for dictionary in data:
            if dictionary["name"] == process.Name and dictionary["sid"] == 0:
                return print(f"\033[32m| [SEGURO] Processo {process.Name} conhecido (já analisado pelo sistema)")
    print(f"\033[33m| [SUSPEITO] Processo {process.Name} desconhecido")
    instance_analysis(process)


def constant_mode():
    print("\033[36m| [AVISO] Modo constante: LIGADO")
    try:
        wmi_service = wmi.WMI()
        watcher = wmi_service.Win32_Process.watch_for("creation")
        while checkbox_state == 1:
            process = watcher()
            on_new_process_created(process)
            analyse(process)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")
    except KeyboardInterrupt:
        print("\033[36m| [AVISO] Modo constante: Desligado\033[0m")


def stop_constant_mode():
    global checkbox_state
    checkbox_state = 0


def start_exe():
    if checkbox_state == 0:
        messagebox.showwarning(
            "Aviso", "Selecione um modo de execução para iniciar")
    else:
        constant_mode()


def main():
    # current_file = os.path.abspath(__file__)

    # if not ctypes.windll.shell32.IsUserAnAdmin():
    #     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, current_file, None, 1)
    #     sys.exit(0)
    
    global features
    features = [
        [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0],

        [1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0], 

        [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], 

        # wannacry standard
        # [0, 0, 1, 1, 1, 1] | [0, 1, 1, 1, 1, 1] | [1, 1, 1, 1, 1, 1]
    ]

    global labels
    labels = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

        2, 2
    ]

    global classif
    classif = tree.DecisionTreeClassifier()
    classif.fit(features, labels)

    global checkbox_state

    while True:
        print("----- Welcome to Aegis -----")
        print("Select a type execution: ")
        try:
            resp = int(input(f"[1] Protect em real time\n[2] Exit\n: "))
            if (resp == 1):
                checkbox_state = 1
                constant_mode()
            elif (resp == 2):
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid type")

# def pywebview():
#     webview.create_window("Aegis Defender", "http://127.0.0.1:5000/", width=1280, height=720, fullscreen=False, maximized=False, confirm_close=True)
#     webview.start()