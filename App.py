from Functions import *
import os
import ctypes
import sys


current_file = os.path.abspath(__file__)

if not ctypes.windll.shell32.IsUserAnAdmin():
    # Executa o programa novamente com privilégios de administrador
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, current_file, None, 1)
    sys.exit(0)

print("=======================================")
print(f"\033[33m| [AVISO] Executando como Administrador")
print("=======================================")

if __name__ == "__main__":
    main()