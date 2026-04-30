class Carrinho:

    def __init__(self):

        self.itens = []
        self.total = 0 
    
    def adicionarItem(self, valor):

        self.itens.append(valor)
        print(f"Item de R${valor} adcionado.")

    def calcularTotal(self):
        self.total = sum(self.itens)
        return self.total 
    
    def exibirCarrinho(self):
        print(f"Itens: {self.itens}")
        print(f"Total: R${self.calcularTotal():.2f}")


#Instanciação
novoCarrinho = Carrinho()
novoCarrinho.adicionarItem(5.00)
novoCarrinho.adicionarItem(20.00)
novoCarrinho.exibirCarrinho()
novoCarrinho.adicionarItem(9.50)
novoCarrinho.exibirCarrinho()
