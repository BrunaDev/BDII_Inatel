class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Motorista:
    def __init__(self, nota: int, corridas: list[Corrida] = None):
        self.nota = nota
        self.corridas = corridas if corridas is not None else []

    def calcular_nota_media(self):
        if not self.corridas:
            return 0.0
        total_notas = sum(corrida.nota for corrida in self.corridas)
        return total_notas / len(self.corridas)