class Chamado:

    def __init__(self, titulo, prioridade,):

        self.titulo = titulo
        self.prioridade = prioridade
        self.status = "Aberto"

    def abrirChamado(self):

        print(f"Chamado {self.titulo} aberto!")

    def fecharChamado(self):

        self.status = "Fechado"
        print(f"Chamado {self.titulo} fechado!")

    def exibirChamados(self):
        
        print(f"Titulo: {self.titulo}")
        print(f"Prioridade: {self.prioridade}")
        print(f"Status: {self.status}")

#INSTANCIAÇÃO

novoChamado = Chamado("Internet parou de funcionar", "Urgente")
novoChamado.abrirChamado()
novoChamado.exibirChamados()
novoChamado.fecharChamado()
