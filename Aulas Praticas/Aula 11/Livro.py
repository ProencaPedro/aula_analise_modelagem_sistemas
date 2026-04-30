class Livro:
    def __init__(self, titulo, autor):

        self.titulo = titulo
        self.autor = autor
        self.disponivel = True 

    def emprestar(self):

        if self.disponivel:
            self.disponivel = False 
            print(f"O livro {self.titulo} foi emprestado.")
        else:
            print("O livro já está emprestado.")

    def devolver(self):

        self.disponivel = True 
        print(f"O livro {self.titulo} foi devolvido.")

    def exibirStatus(self):

        status = "Disponivel" if self.disponivel else "Emprestado"
        print(f"{self.titulo} - {status}")


novoLivro = Livro("Narnia", "C.S Lewis")
novoLivro.exibirStatus()
novoLivro.devolver()
