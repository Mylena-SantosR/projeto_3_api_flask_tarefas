# API de Lista de Tarefas com Flask e Frontend Simples

Este é um projeto full-stack simples que consiste em uma API RESTful de backend, construída com Python e Flask, e uma interface de frontend, construída com HTML, CSS e JavaScript puro.

##  Funcionalidades

* **Criar** novas tarefas.
* **Listar** todas as tarefas.
* **Atualizar** o status de uma tarefa (marcar como concluída).
* **Deletar** tarefas.

##  Tecnologias Utilizadas

**Backend:**
* Python
* Flask
* Flask-SQLAlchemy (para interação com o banco de dados)
* Flask-CORS (para permitir a comunicação com o frontend)
* SQLite

**Frontend:**
* HTML5
* CSS3
* JavaScript (com a Fetch API para requisições)

##  Como Executar o Projeto

Siga os passos abaixo para rodar o projeto localmente.

### 1. Backend (A API)

```bash
# 1. Clone o repositório e navegue até a pasta principal
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd nome-da-pasta-do-projeto

# 2. Crie e ative um ambiente virtual
# Para Windows:
python -m venv venv
.\venv\Scripts\activate
# Para macOS/Linux:
# python3 -m venv venv
# source venv/bin/activate

# 3. Instale as dependências necessárias a partir do arquivo requirements.txt
pip install -r requirements.txt

# 4. Crie o banco de dados (só precisa ser executado uma única vez)
flask init-db

# 5. Inicie o servidor da API
flask run

# A API estará rodando em http://127.0.0.1:5000. Deixe este terminal aberto.#

#Com o servidor do backend já rodando, abra a pasta frontend no seu explorador de arquivos e dê um duplo-clique no arquivo index.html.

#Ele será aberto no seu navegador e já estará conectado e pronto para usar a API.#