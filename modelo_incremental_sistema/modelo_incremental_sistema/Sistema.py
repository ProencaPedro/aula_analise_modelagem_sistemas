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
        print("Aluno cadastrado com sucesso!")

    def listarAlunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado!")
            return
        for aluno in self.alunos:
            print(aluno)

    def cadastrarTarefa(self,idAluno, descricao):
        for aluno in self.alunos:
            if aluno.id == idAluno:
                tarefa = Tarefa(self.contadorTarefa, descricao)
                aluno.adicionarTarefa(tarefa)
                self.contadorTarefa += 1
                print("Tarefa Cadastrada!")
                return
            
        print("Aluno não encontrado!")

    def listarTarefas(self,idAluno):
        for aluno in self.alunos:
            if aluno.id == idAluno:
                aluno.listarTarefas()
                return
        print("Aluno não encontrado.")
        
    def concluirTarefa(self, idAluno, idTarefa):
        for aluno in self.alunos:
            if aluno.id == idAluno:
                for tarefa in aluno.tarefas:
                    if tarefa.id == idTarefa:
                        tarefa.concluida = True
                        print("Tarefa concluida.")
                        return
        print("Tarefa não encontarada.")

    


