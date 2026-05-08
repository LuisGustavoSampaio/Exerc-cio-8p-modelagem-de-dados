#Code Smell: Tipo Primitivo 
#Code Smell: Classe Grande
class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def exibir(self):
        return (
            f"{self.rua}, {self.numero} - {self.bairro}, "
            f"{self.cidade}/{self.estado} - CEP: {self.cep}"
        )


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def exibir(self):
        return f"({self.ddd}) {self.numero}"


class Funcionario:
    def __init__(self, nome, cargo, salario, endereco, telefone):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco
        self.telefone = telefone

    def exibir_dados(self):
        print(f"Funcionário: {self.nome} - {self.cargo}")
        print(f"Salário: R$ {self.salario}")
        print(f"Contato: {self.telefone.exibir()}")
        print(f"Endereço: {self.endereco.exibir()