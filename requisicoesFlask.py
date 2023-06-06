import numpy as np
from flask import Flask, request, render_template, make_response
import joblib
import sklearn.externals


app = Flask(__name__)
model = joblib.load('templates/arquivo.pkl')


@app.route('/')
def exibir_gui():
    return render_template('projeto.html', partial='time.html')


@app.route('/solicitacao', methods=['POST'])
def solicitacao():
    duracao = str(request.form['dur_emp'])
    status_emp = str(request.form['status_emp'])
    valor_emprestimo = str(request.form['money'])
    poupanca = str(request.form['valor'])
    tempo_empregado = str(request.form['tempo'])
    sexo = str(request.form['Sexo'])
    idade = str(request.form['idade'])
    moradia = str(request.form['moradia'])
    situacao_trabalho = str(request.form['situacao_trabalho'])

    dados_usuario = np.array([[duracao, status_emp, valor_emprestimo, poupanca,
                               tempo_empregado, sexo, idade, moradia,situacao_trabalho]])

    resultado = model.predict(dados_usuario)

    if resultado[0] == 0:
        classe = 'Aprovado'
    else:
        classe = 'Reprovado'

    # Renderize o template 'resultado.html' e passe a classe como argumento
    return render_template('projeto.html', classe=classe)


def exibir_time():
    return render_template('time.html')


if __name__ == '__main__':
    app.run('localhost', 9090)
