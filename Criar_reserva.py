#1. Lista longa de parâmetros:
#A função criar_reserva recebe muitos parâmetros, tornando sua chamada difícil de entender e aumentando o risco de erro.

#2. Obsessão por tipos primitivos:
#Dados relacionados ao hóspede, quarto e reserva estão representados por tipos primitivos soltos, como string, int, float e bool, quando poderiam ser agrupados em classes.

#. Método/Função longa:
#A função criar_reserva concentra várias responsabilidades, como exibir dados, calcular diárias, calcular adicionais e mostrar o total.
from datetime import date


class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Quarto:
    def __init__(self, numero, tipo, valor_diaria):
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = valor_diaria


class Reserva:
    def __init__(self, hospede, quarto, data_checkin, data_checkout, possui_cafe_da_manha):
        self.hospede = hospede
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.possui_cafe_da_manha = possui_cafe_da_manha

    def calcular_total_dias(self):
        return (self.data_checkout - self.data_checkin).days

    def calcular_total(self):
        total_dias = self.calcular_total_dias()
        total = total_dias * self.quarto.valor_diaria

        if self.possui_cafe_da_manha:
            total += 50 * total_dias

        return total

    def exibir_reserva(self):
        print(f"Reserva criada para {self.hospede.nome} CPF: {self.hospede.cpf}")
        print(f"Quarto {self.quarto.numero} - {self.quarto.tipo}")
        print(f"De {self.data_checkin} até {self.data_checkout}")
        print(f"Total a pagar: R$ {self.calcular_total():.2f}")
