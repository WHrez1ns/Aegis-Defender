import tkinter as tk
from tkinter import ttk, messagebox
import psutil
from Process import Process
from Event import Event


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


def show_help():
    messagebox.showinfo("Manual", "Modos de execução:\n\n - Modo de verificação: este modo é responsável por analisar o próximo processo que for executado na máquina e determinar se ele é um possível malware.\n - Modo constante: este modo é responsável por verificar todos os processos que forem executados na máquina e determinar se eles podem ser possíveis malwares.\n\nComo usar:\n\n1. Selecione a caixa correspondente ao modo de execução desejado.\n2. Clique em 'Iniciar execução'.\n\nDúvidas? Entre em contato: contato@aegisdefender.org")


def show_alert():
    resposta = messagebox.askyesno(
        "Pergunta", "Você deseja fazer backup dos dados? (Recomendado)")
    if resposta:
        print("Iniciando backup...")
    else:
        messagebox.showinfo("Alerta", "Certo, você optou por não realizar o backup dos dados neste momento. Lembre-se de que essa opção pode ser selecionada posteriormente, caso você queira fazer o backup dos seus dados para garantir sua segurança. Recomendamos que você faça o backup regularmente para evitar a perda de informações importantes. Se surgir a necessidade, você pode acessar a opção de backup nas configurações do Aegis Defender. Fique à vontade para escolher essa opção sempre que considerar apropriado")


def verify_mode():
    print("Modo de verificação ativo...")


def constant_mode():
    print("Modo constante ativo...")


def start_exe():
    if checkbox1_state.get() == checkbox2_state.get():
        messagebox.showwarning(
            "Aviso", "Selecione um modo de execução para iniciar")
        return

    try:
        if checkbox1_state.get() == 1:
            verify_mode()
        else:
            constant_mode()
    except:
        pass

# messagebox.showerror("Erro", "O arquivo selecionado não é um arquivo Excel (.xlsx)")
# messagebox.showwarning("Aviso", "Selecione uma opção de orientação para salvar como PDF")


processos_lista = []
processos = psutil.process_iter()
mapping_processes()

root = tk.Tk()
icon = "img/aegis.ico"
root.iconbitmap(icon)
show_alert()
root.title("Aegis Defender")
root.geometry("400x200")
menubar = tk.Menu(root)
menu_principal = tk.Menu(menubar, tearoff=0)
menu_principal.add_command(label="Ajuda", command=show_help)
menu_principal.add_command(label="Backup", command=show_alert)
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
