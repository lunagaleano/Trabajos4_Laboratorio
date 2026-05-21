'''Ejercicio 4: Define una clase abstracta Notificacion con un método abstracto enviar().
Crea dos clases concretas, Email y SMS, que implementen el método enviar() de manera diferente'''

from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self):
        pass

class Email(Notificacion):
    def enviar(self):
        return "La notificacion fue enviada"

class SMS(Notificacion):
    def enviar(self):
        return "La notificacion fue enviada"