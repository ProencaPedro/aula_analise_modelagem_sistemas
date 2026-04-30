class Veiculo:

    def __init__(self, placa, modelo):
        
        self.placa = placa
        self.modelo = modelo
        self.estacionado = False

    def entrar(self):

        self.estacionado = True
        print(f"Veiculo {self.placa} entrou no estacionamento.")
        
    def sair(self):

        self.estacionado = False
        print(f"Veiculo {self.placa} saiu do estacionamento.")

    def exibirStatus(self):
        
        status = "Estacionado" if self.estacionado else "Fora"
        
        print(f"{self.modelo} ({self.placa}) - {status}")


#Teste

novoVeiculo = Veiculo("WBT5288", "Gol 1.8 Turbo")
novoVeiculo.exibirStatus()
novoVeiculo.entrar()
novoVeiculo.exibirStatus()
novoVeiculo.sair
