class Tarefa:
    def __init__(self, id, descricao):
        if not descricao.strip():
            raise ValueError("Descrição para tarafe não pode ser vazia.")
    
        self.id = id
        self.descricao = descricao
        self.concluida = False  

    def __str__(self):
        status = "Ok" if self.concluida else "X"
        return f"{self.id} - {self.descricao} [{status}]"
