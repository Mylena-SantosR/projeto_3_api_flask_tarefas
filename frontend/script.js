// Endereço da nossa API
const API_URL = 'http://127.0.0.1:5000';

// Elementos da página
const listaDeTarefas = document.getElementById('listaDeTarefas');
const inputNovaTarefa = document.getElementById('inputNovaTarefa');
const btnAdicionar = document.getElementById('btnAdicionar');

// --- FUNÇÕES DE INTERAÇÃO COM A API ---

// 1. Carregar todas as tarefas e exibir na tela
async function carregarTarefas() {
    const response = await fetch(`${API_URL}/tarefas`);
    const tarefas = await response.json();

    listaDeTarefas.innerHTML = ''; // Limpa a lista antes de adicionar os itens

    tarefas.forEach(tarefa => {
        const item = document.createElement('li');
        item.className = 'tarefa-item';
        if (tarefa.concluida) {
            item.classList.add('concluida');
        }

        const descricao = document.createElement('span');
        descricao.className = 'descricao';
        descricao.textContent = tarefa.descricao;
        // Evento para marcar/desmarcar tarefa como concluída
        descricao.addEventListener('click', () => marcarComoConcluida(tarefa.id, !tarefa.concluida));
        
        const btnDeletar = document.createElement('button');
        btnDeletar.textContent = 'Deletar';
        // Evento para deletar a tarefa
        btnDeletar.addEventListener('click', () => deletarTarefa(tarefa.id));

        item.appendChild(descricao);
        item.appendChild(btnDeletar);
        listaDeTarefas.appendChild(item);
    });
}

// 2. Adicionar uma nova tarefa
async function adicionarTarefa() {
    const descricao = inputNovaTarefa.value;
    if (descricao.trim() === '') {
        alert('Por favor, digite uma descrição para a tarefa.');
        return;
    }

    await fetch(`${API_URL}/tarefas`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ descricao: descricao }),
    });

    inputNovaTarefa.value = ''; // Limpa o campo de input
    carregarTarefas(); // Recarrega a lista
}

// 3. Marcar uma tarefa como concluída/não concluída
async function marcarComoConcluida(id, status) {
    await fetch(`${API_URL}/tarefas/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ concluida: status }),
    });
    carregarTarefas(); // Recarrega a lista
}

// 4. Deletar uma tarefa
async function deletarTarefa(id) {
    await fetch(`${API_URL}/tarefas/${id}`, {
        method: 'DELETE',
    });
    carregarTarefas(); // Recarrega a lista
}

// --- EVENTOS ---

// Adiciona evento ao botão "Adicionar"
btnAdicionar.addEventListener('click', adicionarTarefa);

// Carrega as tarefas assim que a página é aberta
carregarTarefas();