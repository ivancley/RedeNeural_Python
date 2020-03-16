class Paciente:
    def __init__(self, nome, febreM, febreA, tosseP, tosseS, fdeAr, dparaResp, pGastrico, diarreia, infectado=False):
        self.nome = nome
        self.febreM = febreM
        self.febreA = febreA
        self.tosseP = tosseP
        self.tosseS = tosseS
        self.fdeAr = fdeAr
        self.dparaResp = dparaResp
        self.pGastrico = pGastrico
        self.diarreia = diarreia
        self.infectado = infectado

    def getDados(self):
        return [[self.febreM, self.febreA, self.tosseP, self.tosseS, self.fdeAr, self.dparaResp, self.pGastrico, self.diarreia]]

    def informar(self):
        return [[self.febreM, self.febreA, self.tosseP, self.tosseS, self.fdeAr, self.dparaResp, self.pGastrico, self.diarreia]]

    def imprimir(self):
        infectado = self.infectado == 1
        print("{}, Infectado {}".format(self.nome, infectado))
