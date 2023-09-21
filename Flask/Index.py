from Functions import *
import ctypes
import sys

def start_app():
    current_file = os.path.abspath(__file__)

    if not ctypes.windll.shell32.IsUserAnAdmin():
         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, current_file, None, 1)
         sys.exit(0)

    webview.create_window("Aegis Defender", "http://127.0.0.1:5000/", width=1280, height=720, fullscreen=False, maximized=False, confirm_close=True)
    webview.start()

start_app()