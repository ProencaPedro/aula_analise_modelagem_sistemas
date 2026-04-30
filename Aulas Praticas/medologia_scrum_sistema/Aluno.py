class Aluno:
    def __init__(self, id, nome):
        if not nome.strip():
            raise ValueError("Nome não pode ser vazio.")
        
        self.id = id
        self.nome = nome
        self.tarefas = []
    

    def adicionarTarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listarTarefas(self):
        return self.tarefas




    def __str__(self):
        return f"{self.id} - {self.nome}"