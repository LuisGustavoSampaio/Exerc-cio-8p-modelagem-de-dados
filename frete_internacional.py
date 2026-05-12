# Message Chain
class Pais:
    def __init__(self, nome):
        self.nome = nome

    def eh_brasil(self):
        return self.nome == "Brasil"


class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

    def pertence_ao_brasil(self):
        return self.pais.eh_brasil()


class Endereco:
    def __init__(self, rua, estado):
        self.rua = rua
        self.estado = estado

    def eh_endereco_nacional(self):
        return self.estado.pertence_ao_brasil()


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def mora_no_brasil(self):
        return self.endereco.eh_endereco_nacional()


class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def eh_pedido_nacional(self):
        return self.cliente.mora_no_brasil()


def verificar_frete_internacional(pedido):
    if pedido.eh_pedido_nacional():
        print("Frete nacional padrão.")
    else:
        print("Sujeito a taxa de importação.")