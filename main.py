import tkinter as tk
from tkinter import filedialog, messagebox
import psutil
from Process import Process


def check_one_checked():
    if checkbox1_state.get() == 1:
        checkbox2.deselect()


def check_two_checked():
    if checkbox2_state.get() == 1:
        checkbox1.deselect()


def mapping_processes():
    for processo in processos:
        try:
            new_process = Process(
                processo.name(), processo.pid, processo.status())
            processos_lista.append(new_process)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


processos_lista = []
processos = psutil.process_iter()
mapping_processes()
for processo in processos_lista:
    print(processo)

root = tk.Tk()
icon = "img/aegis.ico"
root.iconbitmap(icon)
root.title("Aegis Defender")
root.geometry("400x200")

checkbox1_state = tk.BooleanVar()
checkbox2_state = tk.BooleanVar()

label_frame = tk.LabelFrame(root, text="Execution modes:")
label_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label = tk.Label(label_frame, text="Verify mode")
label.grid(row=0, column=0, padx=6, pady=6)

checkbox1 = tk.Checkbutton(label_frame, text="mark",
                           variable=checkbox1_state, command=check_one_checked)
checkbox1.grid(row=0, column=1, padx=5, pady=5)

label = tk.Label(label_frame, text="Constant mode")
label.grid(row=1, column=0, padx=6, pady=6)

checkbox2 = tk.Checkbutton(label_frame, text="mark",
                           variable=checkbox2_state, command=check_two_checked)
checkbox2.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(
    root, text="Start execution")
button.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
