class Item:
    def __init__(self, nome:str, key: int):
        self.nome = nome
        self.key = key

    def __repr__(self):
        return f'Item -> Nome: {self.nome}, key: {self.key} \n'

def ordem(k):
    return k.key

Itens = [
    Item("bill", 3),
    Item("neil", 4),
    Item("john", 2),
    Item("rick", 5),
    Item("alex", 1)
]

Itens.sort(key = ordem)
print(Itens)
