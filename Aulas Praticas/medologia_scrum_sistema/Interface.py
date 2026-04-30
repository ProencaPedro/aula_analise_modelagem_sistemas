import tkinter as tk
from tkinter import messagebox
from Sistema import Sistema 

    
class Interface:
    def __init__(self):
        self.sistema = Sistema()

        self.janela = tk.Tk()

        self.janela.title("Sistema 2° Semestre")
        self.janela.geometry("450x400")

        #Criação das Etiquetas
        tk.Label(self.janela, text="Nome do Aluno").pack()
        self.nomeEntry = tk.Entry(self.janela, width=40)             
        self.nomeEntry.pack()   

        tk.Label(self.janela, text="Descrição da Tarefa").pack()
        self.tarefaEntry = tk.Entry(self.janela, width=50)
        self.tarefaEntry.pack()

        #Criação dos Botões
        tk.Button(self.janela, text="Cadastrar Aluno", command=self.cadastrarAluno).pack()
        tk.Button(self.janela, text="Listar Alunos", command=self.listarAlunos).pack()
        tk.Button(self.janela, text="Cadastrar Tarefa", command=self.cadastrarTarefa).pack()

        self.lista = tk.Listbox(self.janela)
        self.lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        #Lista de Tarefas 
        tk.Label(self.janela, text="Tarefas do Aluno").pack()
        self.listaTarefas = tk.Listbox(self.janela, height=10)
        self.listaTarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        tk.Button(self.janela, text="Concluir Tarefa", command=self.concluirTarefa).pack()

        tk.Button(self.janela, text="Listar Tarefa do Aluno", command=self.listarTarefas).pack()
        


        self.janela.mainloop()

    def cadastrarAluno(self):
        nome = self.nomeEntry.get()

        if nome.strip():
            try:
                self.sistema.cadastrarAluno(nome)
                messagebox.showinfo("Sucesso","Aluno cadastrado com sucesso!")
                self.listarAlunos()

            except ValueError as e:
                messagebox.showerror("Erro", str(e))

        else:
            messagebox.showerror("Erro", "Nome não pode ser vazio.")

    def listarAlunos(self):
        self.lista.delete(0, tk.END)
        alunos = self.sistema.listarAlunos()

        if not alunos:
            self.lista.insert(tk.END, "Nenhum aluno cadastrado.")
            return
        for aluno in alunos:
            self.lista.insert(tk.END, str(aluno))


    def idAlunoSelecionado(self):
        selecionado = self.lista.curselection()

        if not selecionado:
            return None
        
        texto = self.lista.get(selecionado[0])
        idAluno = int(texto.split("-")[0])
        return idAluno  

    def cadastrarTarefa(self):
        idAluno = self.idAlunoSelecionado()
        descricao = self.tarefaEntry.get()

        if idAluno is None:
            messagebox.showerror("Erro", "Selecione um aluno")
            return
        

        if not descricao.strip():
            messagebox.showerror("Erro","Descrição da tarefa não pode ser vazia.")
            return
        

        try:
            sucesso = self.sistema.cadastrarTarefa(idAluno, descricao)

            if sucesso:
                messagebox.showinfo("Sucesso", "Tarefa cadastrada com sucesso!")
            else:
                messagebox.showerror("Erro", "Aluno não encontrado.")

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    
    def listarTarefas(self):
        self.listaTarefas.delete(0, tk.END)

        idAluno = self.idAlunoSelecionado()

        if idAluno is None:
            messagebox.showerror("Erro", "Selecione um aluno.")
            return
        
        tarefas = self.sistema.listarTarefas(idAluno)

        if not tarefas: 
            self.listaTarefas.insert(tk.END,"Nenhuma tarefa cadastrada.")
        
        for tarefa in tarefas:
            self.listaTarefas.insert(tk.END, str(tarefa))


    def idTarefaSelecionada(self):
        selecionado = self.listaTarefas.curselection()

        if not selecionado:
            return None
        
        texto = self.listarTarefas.get(selecionado[0])
        idTarefa = int(texto.split("-")[0])
        return idTarefa
    



    def concluirTarefa(self):
        idAluno = self.idAlunoSelecionado()
        idTarefa = self.idTarefaSelecionada()

        if idAluno is None:
            messagebox.showerror("Erro", "Selecione um aluno.")
            return
        
        if idTarefa is None:
            messagebox.showerror("Erro", "Selecione uma tarefa.")
            return
        
        sucesso = self.sistema.concluirTarefa(idAluno, idTarefa)

        if sucesso:
            messagebox.showinfo("Sucesso", "Tarefa Concluida!")
        else:
            messagebox.showerror("Erro", "Tarefa não encontrada!")

if __name__== "__main__":
    Interface()