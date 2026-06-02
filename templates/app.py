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

nome = request.form['nome']   # Captura o campo nome
idade = request.form['idade'] # Captura o campo idade
curso = request.form['curso'] # Captura o campo curso

# Validaçao de dados
if not nome or not idade or not curso:
    mensagem_resultado = "ERRO: Todos os campos são Obrigatorios!"
else:
    idade_int = int(idade)
    mensagem_base = f"Ola{nome}, você tem {idade} anos e está no curso de {curso}!"
if idade_int < 18:
    mensagem_idade = "Voce e Menor de Idade."
elif idade_int > 18 and idade_int <65:
    mensagem_idade = "Voce é Adulto."
else:
    mensagem_idade = "Você é experiente!."

# Estrutura condicional para o Curso

    if curso: == "Python":
    mensagem_curso = "Otima escolha, você é versátil!"
    elif curso == "Flask":
    mensagem_curso = "Otima escolha gafanhoto!"
    elif == "HTML/CSS":
    mensagem_curso = "Fundamental pequenino gafanhoto"
else:
    mensagem_curso = "Curso Interressante"
    mensagem_resultado = f"{mensagem_curso}\n{mensagem_idade}\n{mensagem_idade}"

    mensagem_resultado = "Sucesso!\n" mensagem_resultado

return render_template("formulario.html", resultado=mensagem_resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
