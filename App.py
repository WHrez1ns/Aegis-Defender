from flask import Flask, render_template, url_for, make_response
from threading import Thread
import subprocess
from Functions import *

app = Flask(__name__)

# Definindo uma rota para o Flask através de um decorator | decorator: atribui uma nova funcionalidade para a função que vem abaixo
@app.route("/")
def dashboard():
    url_for('static', filename='css/style.css')
    url_for('static', filename='css/colors.css')
    url_for('static', filename='images/aegis-logo.png')
    url_for('static', filename='js/dashboard.js')
    url_for('static', filename='json/process.json')
    url_for('static', filename='boxicons-2.1.4/css/boxicons.min.css')
    return render_template("index.html")

@app.route("/processes")
def processes():
    # url_for('static', filename='css/style.css')
    # url_for('static', filename='css/colors.css')
    # url_for('static', filename='images/aegis-logo.png')
    url_for('static', filename='js/process.js')
    # url_for('static', filename='json/process.json')
    return render_template("processes.html")

@app.route("/starting_application", methods=['GET'])
def starting_app():
    main()
    return make_response(
        "Successful response from API: Starting application"
    )

@app.route("/closing_application", methods=['GET'])
def closing_app():
    stop_mode()
    return make_response(
        "Sucessful response from API: Closing application"
    )

if __name__ == "__main__":
    thread_server = Thread(target=app.run)
    thread_server.start()
    subprocess.Popen("Index.py", shell=True, text=True)