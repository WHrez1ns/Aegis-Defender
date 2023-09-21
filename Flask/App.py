from threading import Thread
from flask import Flask, render_template, url_for
import Functions
import time
import subprocess

app = Flask(__name__)

# Definindo uma rota para o Flask através de um decorator | decorator: atribui uma nova funcionalidade para a função que vem abaixo
@app.route("/")
def dashboard():
    url_for('static', filename='css/style.css')
    url_for('static', filename='css/colors.css')
    url_for('static', filename='images/aegis-logo.png')
    url_for('static', filename='js/dashboard.js')
    url_for('static', filename='json/process.json')
    return render_template("index.html")

@app.route("/processes")
def processes():
    url_for('static', filename='css/style.css')
    url_for('static', filename='css/colors.css')
    url_for('static', filename='images/aegis-logo.png')
    url_for('static', filename='js/process.js')
    url_for('static', filename='json/process.json')
    return render_template("processes.html")

@app.route("/apis")
def apis():
    # Functions.main()
    return "Successful API request"

if __name__ == "__main__":
    thread_server = Thread(target=app.run)
    thread_server.start()
    subprocess.Popen("python Index.py", shell=True, text=True)