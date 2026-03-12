from Sistema import Sistema
from Interface import Interface

sistema = Sistema()

if __name__=="__main__":
    Interface()

while True:
    
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Cadastrar Tarefa")
    print("4. Listar Tarefas")
    print("5. Concluir Tarefa")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        sistema.cadastrarAluno(nome)

    elif opcao == "2":
        sistema.listarAlunos()

    elif opcao == "3":
        idAluno = int(input("ID do Aluno: "))
        descricao = input("Descrição da Tarefa: ")
        sistema.cadastrarTarefa(idAluno, descricao)

    elif opcao == "4":
        idAluno = int(input("ID do Aluno: "))
        sistema.listarTarefas(idAluno)

    elif opcao == "5":
        idAluno = int(input("ID do Aluno: "))
        idTarefa = int(input("ID da Tarefa: "))
        sistema.concluirTarefa(idAluno, idTarefa)
    
    elif opcao == "0":
        break
    else:
        print("Opção inválida. ")

