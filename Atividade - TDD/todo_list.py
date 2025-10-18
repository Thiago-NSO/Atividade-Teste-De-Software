class Tarefa:
    def __init__(self, nome, descricao):
        if not nome:
            raise ValueError("O nome da tarefa não pode ser vazio.")
        self.nome = nome
        self.descricao = descricao
        self.status = "Em andamento"

    def concluir(self):
        self.status = "Concluída"

    def retomar(self):
        self.status = "Em andamento"

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nome, descricao):
        nova_tarefa = Tarefa(nome, descricao)
        self.tarefas.append(nova_tarefa)

    def marcar_como_concluida(self, indice_tarefa):
        self.tarefas[indice_tarefa].concluir()

    def marcar_como_em_andamento(self, indice_tarefa):
        self.tarefas[indice_tarefa].retomar()

    def editar_tarefa(self, indice, novo_nome, nova_descricao):
        if not novo_nome:
            raise ValueError("O nome da tarefa não pode ser vazio.")
        tarefa = self.tarefas[indice]
        tarefa.nome = novo_nome
        tarefa.descricao = nova_descricao

    def excluir_tarefa(self, indice):
        self.tarefas.pop(indice)