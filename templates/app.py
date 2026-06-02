from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/formulario')
def pagina_inicio():
    return render_template('formulario.html', resultado="Aguardando envio...")

@app.route('/processar', methods=['POST'])
def processar_formulario():
    if request.method == 'POST':
