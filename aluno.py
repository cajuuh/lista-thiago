import json


class Aluno:  # classe
    def __init__(self):
        self.nome = ""
        self.notas = []
        self.media = 0

    def __str__(self):
        return str(self.nome)

    def __list__(self):
        return self.notas

    def __float__(self):
        return float(self.media)
