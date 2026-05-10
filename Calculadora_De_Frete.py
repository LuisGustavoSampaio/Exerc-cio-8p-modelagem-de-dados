 #Refatoração orientada a objetos
from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def calcular_frete(self, distancia):
        pass


class Moto(Transporte):
    def calcular_frete(self, distancia):
        return distancia * 2.0


class Carro(Transporte):
    def calcular_frete(self, distancia):
        return distancia * 3.5 + 10.0


class Caminhao(Transporte):
    def calcular_frete(self, distancia):
        return distancia * 8.0 + 50.0


class Bicicleta(Transporte):
    def calcular_frete(self, distancia):
        return distancia * 1.0


class CalculadoraDeFrete:
    def calcular(self, transporte, distancia):
        return transporte.calcular_frete(distancia)