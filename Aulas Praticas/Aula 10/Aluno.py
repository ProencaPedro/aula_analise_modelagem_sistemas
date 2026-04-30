class Aluno:
    def __init__(self, nome, idade, matricula):
        #inicializar atributos no sistema:
        self.nome = nome
        self.idade = idade
        self.matricula = matricula


    #Inserindo os Metodos (Comportamentos)
    def exibirDados(self):
        print("Dados do Aluno")
        print(f"Nome : {self.nome} ")
        print(f"Idade: {self.idade}")
        print(f"Matricula: {self.matricula}")


    #Fazer aniversario(atualizar a idade)
    def fazerAniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome}, agora você tem {self.idade} anos!")

#Instanciação
novoAluno = Aluno("Pedro" ,25, "2026001")
novoAluno.exibirDados()
novoAluno.fazerAniversario()