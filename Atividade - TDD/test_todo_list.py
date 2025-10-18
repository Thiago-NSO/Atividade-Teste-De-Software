import unittest
from todo_list import Tarefa, ListaDeTarefas

class TestListaDeTarefas(unittest.TestCase):

    def test_adicionar_tarefa(self):
        lista = ListaDeTarefas()
        lista.adicionar_tarefa("Estudar TDD", "Aprender o ciclo Red-Green-Refactor")
        self.assertEqual(len(lista.tarefas), 1)
        self.assertEqual(lista.tarefas[0].nome, "Estudar TDD")
        self.assertEqual(lista.tarefas[0].status, "Em andamento")

    def test_nao_deve_adicionar_tarefa_sem_nome(self):
        lista = ListaDeTarefas()
        with self.assertRaises(ValueError):
            lista.adicionar_tarefa("", "Descrição sem nome")

    def test_marcar_tarefa_como_concluida(self):
        lista = ListaDeTarefas()
        lista.adicionar_tarefa("Teste", "Descrição")
        lista.marcar_como_concluida(0)
        self.assertEqual(lista.tarefas[0].status, "Concluída")

    def test_marcar_tarefa_como_em_andamento(self):
        lista = ListaDeTarefas()
        lista.adicionar_tarefa("Teste", "Descrição")
        lista.marcar_como_concluida(0)
        lista.marcar_como_em_andamento(0)
        self.assertEqual(lista.tarefas[0].status, "Em andamento")

    def test_editar_tarefa(self):
        lista = ListaDeTarefas()
        lista.adicionar_tarefa("Nome Antigo", "Desc Antiga")
        lista.editar_tarefa(0, "Nome Novo", "Desc Nova")
        self.assertEqual(lista.tarefas[0].nome, "Nome Novo")
        self.assertEqual(lista.tarefas[0].descricao, "Desc Nova")

    def test_editar_tarefa_inexistente(self):
        lista = ListaDeTarefas()
        with self.assertRaises(IndexError):
            lista.editar_tarefa(0, "Nome", "Desc")

    def test_excluir_tarefa(self):
        lista = ListaDeTarefas()
        lista.adicionar_tarefa("Para excluir", "...")
        lista.excluir_tarefa(0)
        self.assertEqual(len(lista.tarefas), 0)

    def test_excluir_tarefa_inexistente(self):
        lista = ListaDeTarefas()
        with self.assertRaises(IndexError):
            lista.excluir_tarefa(0)

if __name__ == '__main__':
    unittest.main()