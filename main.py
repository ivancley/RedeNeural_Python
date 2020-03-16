import Paciente
from RedeNeural import RedeNeural
from CoronaVirusDAO import CoronaVirusDAO
from Paciente import Paciente

## SISTEMA
# Inicialização
sair = False
dao = CoronaVirusDAO()
rn = RedeNeural("dataset-coronavirus.xlsx")

print("Sistema de triagem de pacientes para testes do Coronavirus ")

while sair == False:
    print('1 - Cadastrar novo paciente')
    print('2 - Gerar relatório ')
    print('3 - Sair do Sistema')
    opcao = int(input('Escolha uma opção:'))
    if opcao == 1:
        nome = input('Informe o nome do paciente: ')
        febreM = int(input("Febre moderada(38 a 39 °C)?  1=Sim, 0=NÃO : "))
        febreA = int(input("Febre alta (acima de 39 °C)? 1=Sim, 0=NÃO : "))
        tosseP = int(input("Tosse Persistente?           1=Sim, 0=NÃO : "))
        tosseS = int(input("Tosse Seca?                  1=Sim, 0=NÃO : "))
        fdeAr = int(input("Falta de Ar?                 1=Sim, 0=NÃO : "))
        dparaResp = int(input("Dor para respirar?           1=Sim, 0=NÃO : "))
        pGastrico = int(input("Problema Gastrico?           1=Sim, 0=NÃO : "))
        diarreia = int(input("Diarreia?                    1=Sim, 0=NÃO : "))
        paciente = Paciente(nome, febreM, febreA, tosseP, tosseS, fdeAr, dparaResp, pGastrico, diarreia)
        paciente.infectado = rn.testar(paciente)

        if paciente.infectado:
            print("------------Paciente possivelmente infectado ")

        dao.salvar(paciente)

    if opcao == 2:
        infectados = 0
        print()
        print("Relatório_________________________________")
        pacientes = dao.listar()
        for paciente in pacientes:
            paciente.imprimir()
            if paciente.infectado == True:
                infectados+=1
        print("Pacientes cadastrados....:{}".format(len(pacientes)))
        print("Pacientes infectados.....:{}".format(infectados))
        print()

    if opcao == 3:
        sair = True
