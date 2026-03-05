import tkinter as tk
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

        self.janela.mainloop()