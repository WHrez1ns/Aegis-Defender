import os
import psutil
import wmi
from sklearn import tree
import json
import time
from pathlib import Path
import pythoncom


def line():
    print("===================================================================")


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
    line()
    print(f"[WARNING] New process found: {process.Name}")


def extensions_analysis(process):
    malicious_extensions = [".fun", ".wnry", ".WNCRY", ".res", ".eky", ".pky",".locked", ".msi", ".bat", ".cmd", ".hta", ".scr", ".pif", ".reg", ".vbs", ".wsf", ".cpl", ".jar"]

    try:
        processid = psutil.Process(process.ProcessId)
        path = Path.home() / "Desktop"
        count = 0

        print(f"[WARNING] Starting extension analysis in the directory: {path}")
        while count <= 180:
            files = os.listdir(path)
            for file in files:
                for extension in malicious_extensions:
                    if file.find(extension) != -1:
                        processid.terminate()
                        print(f"[THREAT] Threat neutralized: {process.Name}")
                        new_item_in_json("static/json/process.json", process.Name, 2)
                        return print(f"[DANGEROUS] File with malicious or compromised extension identified: {file} | Status id: 2")
                    else:
                        count += 1
            time.sleep(1.5)
        print("[SAFE] No files with malicious or compromised extension identified")
        new_item_in_json("static/json/process.json", process.Name, 0)
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
                print(f"[SUSPECT] {key} >= {threshold}: {value}")
                status_list.append(1)
            else:
                print(f"[SAFE] {key} < {threshold}: {value}")
                status_list.append(0)
        print(f"[VERIFICATION] Status list: {status_list}")
        status_id = classif.predict([status_list])
        if status_id == 2:
            processid.terminate()
            print(f"[DANGEROUS] Threat neutralized: {process.Name} | Status id: 2")
            new_item_in_json("static/json/process.json", process.Name, 2)
        elif status_id == 1:
            print(f"[SUSPECT] Process has suspicious behavior: {process.Name} | Status id: 1")
            extensions_analysis(process)
        else:
            print(f"[SAFE] Status id: 0 | {process.Name}")
            extensions_analysis(process)
    except psutil.NoSuchProcess:
        print(f"[SUSPECT] Process {process.Name} not found")
    except psutil.AccessDenied:
        print(f'[SUSPECT] Permission denied to close the process {process.Name}')
    except IndexError:
        print(f"[SUSPECT] Process {process.Name} not found")
    except wmi.x_wmi:
        print(f'[SUSPECT] Permission denied to close the process {process.Name}')
    except Exception as e:
        print(e)


def analyse(process):
    try:
        processid = psutil.Process(process.ProcessId)

        with open("static/json/process.json", 'r') as file:
            data = json.load(file)
            for dictionary in data:
                if dictionary["name"] == process.Name and dictionary["sid"] == 0:
                    return print(f"[SAFE] Process {process.Name} known (already analyzed by the system)")
                elif dictionary["name"] == process.Name and dictionary["sid"] == 2:
                    processid.terminate()
                    return print(f"[DANGEROUS] Threat {process.Name} known (neutralized by the system)")
                else:
                    continue
            print(f"[SUSPECT] Process {process.Name} unknown")
            instance_analysis(process)
    except Exception as e:
        print(e)


def constant_mode(state):
    line()
    print("[WARNING] Real-time detection: ON")
    try:
        wmi_service = wmi.WMI()
        watcher = wmi_service.Win32_Process.watch_for("creation")
        while state == True:
            process = watcher()
            on_new_process_created(process)
            analyse(process)
    except KeyboardInterrupt:
        line()
        print("[WARNING] Real-time detection: OFF")
        pythoncom.CoUninitialize()
    except Exception as e:
        print(f"Erro: {e}")


def stop_mode():
    print("[WARNING] Real-time detection: TRYING TO FINISH")


def main():
    pythoncom.CoInitialize()

    global features, labels, classif, button_state
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

    button_state = True
    constant_mode(button_state)