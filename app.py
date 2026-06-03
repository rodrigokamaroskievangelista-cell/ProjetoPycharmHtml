from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/formulario')
def exibir_formulario():
    return render_template('formulario.html', resultado='Aguardando o envio...')


@app.route('/processar', methods=['POST'])
def processar_formulario():

    """ Esta função recebe os dados enviados pelo formulário,
    processa-os com estruturas condicionais e retorna
    uma mensagem personalizada. """

    """ Capturas os dados do Formulario
    request.form e um dicionario com todos os campos enviados
    O nome entre colchetes deve ser igual ao "nome" do campo formulario
    HTML """

    # Captura os dados
    nome = request.form.get('nome')   # Captura o campo nome
    idade = request.form.get('idade') # Captura o campo idade
    curso = request.form.get('curso') # Captura o campo curso

    # Validação
    if not nome or not idade or not curso:
        mensagem_resultado = f"ERRO: Todos os campos são obrigatórios! (nome={nome}, idade={idade}, curso={curso})"
    else:
        idade_int = int(idade)
        mensagem_base = f"Olá {nome}, você tem {idade} anos e está no curso de {curso}!"

        if idade_int < 18:
            mensagem_idade = "Você é menor de idade."
        elif idade_int < 60:
            mensagem_idade = "Você é adulto."
        else:
            mensagem_idade = "Você é experiente!"

        # Estrutura condicional para o Curso

        if curso == "Python":
            mensagem_curso = "Ótima escolha! Python é versátil!"
        elif curso == "Flask":
            mensagem_curso = "Excelente escolha! Flask é incrível!"
        elif curso == "HTML/CSS":
            mensagem_curso = "Fundamental! HTML/CSS é a base da web!"
        else:
            mensagem_curso = "📚 Curso interessante!"

        mensagem_resultado = f"{mensagem_base}\n{mensagem_idade}\n{mensagem_curso}"

    return render_template('formulario.html', resultado=mensagem_resultado)

#final
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)