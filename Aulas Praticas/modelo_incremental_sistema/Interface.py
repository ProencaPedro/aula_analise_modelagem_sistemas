import tkinter as tk
from tkinter import messagebox
from Sistema import Sistema

class Interface:
    def __init__(self):
        self.sistema = Sistema()

        self.janela = tk.Tk()
        self.janela.title("System")
        self.janela.geometry("400x400")

        tk.Label(self.janela, text="Nome do Aluno").pack()
        self.nomeEntry = tk.Entry(self.janela)
        self.nomeEntry.pack()

        tk.Label(self.janela, text="Descrição da Tarefa").pack()
        self.tarefaEntry = tk.Entry(self.janela)
        self.tarefaEntry.pack()


        tk.Button(self.janela, text="Cadastrar Aluno", command=self.cadastrarAluno).pack()
        tk.Button(self.janela, text="Listar Alunos", command=self.listarAlunos).pack()
        tk.Button(self.janela, text="Cadastrar Tarefa", command=self.cadastrarTarefa).pack()

        self.lista = tk.Listbox (self.janela)
        self.lista.pack(fill=tk.BOTH, expand=True)
        

        self.janela.mainloop()

    def cadastrarAluno(self):
        nome = self.nomeEntry.get()
        if nome:
            self.sistema.cadastrarAluno(nome)
            messagebox.showinfo("Sucesso","Aluno Cadastrado!")
            self.nomeEntry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro","Nome não pode ser vazio. ")

    def listarAlunos(self):
        self.lista.delete(0, tk.END)
        for aluno in self.sistema.listarAlunos():
            self.lista.insert(tk.END, f"{aluno.id} - {aluno.nome}")

    def cadastrarTarefa(self):
        selecionado = self.lista.curselection()

        if not selecionado:
            messagebox.showerror("Erro", "Selecione um aluno")
            return
        
        alunoTexto = self.lista.get(selecionado)
        
        idAluno = int(alunoTexto.split(" - ")[0])

        descricao = self.tarefaEntry.get()

        if descricao:
            self.sistema.cadastrarTarefa(idAluno, descricao)
            messagebox.showinfo("Sucesso", "Tarefa Cadastrada!")
            self.tarefaEntry.delete(0, tk.END)
        
        else:
            messagebox.showerror("Erro", "Digite uma descrição")





