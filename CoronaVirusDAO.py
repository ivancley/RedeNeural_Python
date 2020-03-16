import sqlite3
from Paciente import Paciente

class CoronaVirusDAO:
    def __init__(self):
        self.connection = sqlite3.connect('coronavirus.db')
        self.cursor = self.connection.cursor()
        #criarbanco
        self.cursor.execute('CREATE TABLE IF NOT EXISTS pacientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome INT, febreM INT, febreA INT, tosseP INT, tosseS INT, fdeAr INT, dparaResp INT, pGastrico INT, diarreia INT, infectado INT);')

    def salvar(self, p):
        self.cursor.execute("INSERT INTO pacientes (nome, febreM, febreA, tosseP, tosseS, fdeAr, dparaResp, pGastrico, diarreia, infectado) VALUES(?,?,?,?,?,?,?,?,?,?);",(p.nome, p.febreM, p.febreA, p.tosseP, p.tosseS, p.fdeAr, p.dparaResp, p.pGastrico, p.diarreia, p.infectado))
        self.connection.commit()

    def listar(self):
        _pacientes = self.cursor.execute("SELECT * FROM pacientes ORDER BY nome")
        pacientes = []
        for r in _pacientes:
            p = Paciente(r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10])
            pacientes.append(p)
        return pacientes
