from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 

# Inicializa o Flask
app = Flask(__name__)
CORS(app) 

# Configura o banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Modelo do Banco de Dados ---
# Define a estrutura da nossa tabela 'tarefa'
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    concluida = db.Column(db.Boolean, default=False, nullable=False)

    # Função para transformar nosso objeto Tarefa em um dicionário (e depois JSON)
    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'concluida': self.concluida
        }

# --- Rotas da API (Nossos "Endereços") ---

# Rota para obter todas as tarefas (GET /tarefas)
@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = Tarefa.query.all()
    # Converte a lista de tarefas para uma lista de dicionários
    return jsonify([tarefa.to_dict() for tarefa in tarefas])

# Rota para criar uma nova tarefa (POST /tarefas)
@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    # Pega os dados JSON enviados na requisição
    dados = request.get_json()
    if not dados or 'descricao' not in dados:
        return jsonify({'erro': 'Descrição da tarefa é obrigatória'}), 400

    nova_tarefa = Tarefa(descricao=dados['descricao'])
    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify(nova_tarefa.to_dict()), 201

# Rota para atualizar uma tarefa (marcar como concluída) (PUT /tarefas/<id>)
@app.route('/tarefas/<int:id>', methods=['PUT'])
def update_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    dados = request.get_json()

    tarefa.concluida = dados.get('concluida', tarefa.concluida)
    db.session.commit()
    return jsonify(tarefa.to_dict())

# Rota para deletar uma tarefa (DELETE /tarefas/<id>)
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def delete_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({'mensagem': 'Tarefa deletada com sucesso'}), 200

# --- Comando para inicializar o banco de dados ---
@app.cli.command('init-db')
def init_db_command():
    """Cria as tabelas do banco de dados."""
    with app.app_context():
        db.create_all()
    print('Banco de dados inicializado.')

# Permite rodar o app com 'python app.py'
if __name__ == '__main__':
    app.run(debug=True)