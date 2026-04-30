import json

def salvar(dados):
    with open("dados.json","w") as f:
        json.dump(dados, f)


def carregar():
    try:
        with open("dados.jason","r") as f:
            return json.load(f)
    except:
        return {}