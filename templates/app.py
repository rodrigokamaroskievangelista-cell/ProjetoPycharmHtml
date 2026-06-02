from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/formulario')
def pagina_inicio():
    return render_template('formulario.html', resultado="Aguardando envio...")

@app.route('/processar', methods=['POST'])
def processar_formulario():
    if request.method == 'POST':

""" Esta função recebe os dados enviados pelo formulário,
 processa-os com estruturas condicionais e retorna
 uma mensagem personalizada. """

""" Capturas os dados do Formulario
 request.form e um dicionario com todos os campos enviados
 O nome entre colchetes deve ser igual ao "nome" do campo formulario
 HTML """

nome = request.form['nome'] # Captura o campo nome
idade = request.form['idade'] # Captura o campo idade
curso = request.form['curso'] # Captura o campo curso