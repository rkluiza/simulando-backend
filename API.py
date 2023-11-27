from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from operacoes_banco import *
from models import *

app = Flask(__name__)
CORS(app)

#endpoint para obter todos os usuarios existentes
@app.route("/usuariosExistentes", methods=["GET"])
def obter_UsuariosExistentes():
    usuarios = obterUsuariosExistentes()
    return jsonify(usuarios)



app.run()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def get_questions():
    questao = Question.select()
    choices = Choice.select()
    data = []
    for q in questions:
        choices_data = [c for c in choices if c.question == q.question_text]
        data.append({
            'question': q.question_text,
            'choices': [{'text': c.is_correct, 'correct': c.is_correct == 'true'} for c in choices_data]
        })
    return jsonify({'questions': data})

if __name__ == '__main__':
    app.run(debug=True)