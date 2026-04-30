from Aluno import Aluno
from Tarefa import Tarefa 

class Sistema:
    def __init__(self):
        self.alunos = []
        self.contadorAluno = 1 
        self.contadorTarefa = 1


    def cadastrarAluno(self, nome):
        aluno = Aluno(self.contadorAluno, nome)
        self.alunos.append(aluno)
        self.contadorAluno += 1


    def listarAlunos(self):
        return self.alunos


    def buscarAluno(self, idAluno):
        for aluno in self.alunos:
            if aluno.id == idAluno:
                return aluno
            return None
        
    def cadastrarTarefa(self, idAluno, descricao):
        aluno = self.buscarAluno(idAluno)

        if aluno:
            tarefa = Tarefa(self.contadorTarefa, descricao)
            aluno.adicionarTarefa(tarefa)
            self.contadorTarefa += 1 
            return True 
        return False
    

    def listarTarefas(self, idAluno):
        aluno = self.buscarAluno(idAluno)

        if aluno:
            return aluno.listarTarefas()
        

    def buscarTarefa(self, aluno, idTarefa):
        for tarefa in aluno.tarefas:
            if tarefa.id == idTarefa:
                return tarefa

            return None
    

    def concluirTarefa(self, idAluno, idTarefa):
        aluno = self.buscarTarefa(aluno, idTarefa)

        if aluno:
            tarefa = self.buscarTarefa(aluno, idTarefa)

            if tarefa:
                tarefa.concluir = True
                return True
        return False