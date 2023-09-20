import os
import ctypes
import sys
from tkinter import messagebox
import psutil
import wmi
from sklearn import tree
import json
import webview
import time
from threading import Thread


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
    print("===================================================")
    print(f"[AVISO] Novo processo encontrado: {process.Name}")


def extensions_analysis(process):
    malicious_extensions = [".wnry", ".locked", ".msi", ".bat", ".cmd", ".hta", ".scr", ".pif", ".reg", ".vbs", ".wsf", ".cpl", ".jar"]
    try:
        processid = psutil.Process(process.ProcessId)
        path = os.getcwd()
        count = 0

        print(f"[AVISO] Iniciando análise de extensões no diretório: {path}")
        while count <= 50:
            files = list(filter(os.path.isfile, os.listdir(path)))
            for file in files:
                for extension in malicious_extensions:
                    if file.find(extension) != -1:
                        processid.terminate()
                        print(f"[PERIGOSO] Arquivo com extensão maliciosa ou suspeita identificado: {process.Name} | Status id: 2")
                        new_item_in_json("static/json/process.json", process.Name, 2)
                        count = 50
                    else:
                        print("[SEGURO] Nenhum arquivo com extensão maliciosa ou suspeita identificado")
                        count += 1
            time.sleep(1.5)
    except Exception as e:
        print(e)


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
                print(f"[SUSPEITO] {key} >= {threshold}: {value}")
                status_list.append(1)
            else:
                print(f"[SEGURO] {key} < {threshold}: {value}")
                status_list.append(0)
        print(f"[VERIFICAÇÃO] Status list: {status_list}")
        status_id = classif.predict([status_list])
        if status_id == 2:
            processid.terminate()
            print(f"[PERIGOSO] Ameaça neutralizada: {process.Name} | Status id: 2")
            new_item_in_json("process.json", process.Name, 2)
        elif status_id == 1:
            print(f"[SUSPEITO] Processo possui um comportamento suspeito: {process.Name} | Status id: 1")
            extensions_analysis(process)
            # new_item_in_json("static/json/process.json", process.Name, 1)
        else:
            print(f"[SEGURO] Status id: 0 | {process.Name}")
            extensions_analysis(process)
            # new_item_in_json("static/json/process.json", process.Name, 0)
    except psutil.NoSuchProcess:
        print(f"[SUSPEITO] Processo {process.Name} não encontrado")
    except psutil.AccessDenied:
        print(f'[SUSPEITO] Permissão negada para encerrar o processo {process.Name}')
    except IndexError:
        print(f"[SUSPEITO] Processo {process.Name} não encontrado")
    except wmi.x_wmi:
        print(f'[SUSPEITO] Permissão negada para encerrar o processo {process.Name}')


def analyse(process):
    with open("static/json/process.json", 'r') as file:
        data = json.load(file)
        for dictionary in data:
            if dictionary["name"] == process.Name and dictionary["sid"] == 0:
                return print(f"[SEGURO] Processo {process.Name} conhecido (já analisado pelo sistema)")
    print(f"[SUSPEITO] Processo {process.Name} desconhecido")
    instance_analysis(process)


def constant_mode():
    print("[AVISO] Modo constante: LIGADO")
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
        stop_constant_mode()
        print("[AVISO] Modo constante: Desligado\033[0m")


def stop_constant_mode():
    global checkbox_state
    checkbox_state = 0


def main():
    global features, labels, classif, checkbox_state
    features = [
        [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0],

        [1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0], 

        [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], 

        # wannacry standard
        # [0, 0, 1, 1, 1, 1] | [0, 1, 1, 1, 1, 1] | [1, 1, 1, 1, 1, 1]
    ]

    labels = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

        2, 2
    ]

    classif = tree.DecisionTreeClassifier()
    classif.fit(features, labels)

    print("===================================================")
    print("|             Aegis Defender - 4.2.0              |")
    print("===================================================")
    while True:
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