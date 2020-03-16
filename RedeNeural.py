import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from Paciente import Paciente

class RedeNeural:
    def __init__(sefl, baseDeDados):
        print("Carregando dados")
        excel_file = baseDeDados
        base = pd.read_excel(excel_file, encoding = 'latin−1')
        # estão em todas as linhas da coluna 8
        respostas = base.iloc[:, 8].values
        # estão em todas as linhas até a coluna 8
        dados = base.iloc[:, :8].values
        # anotação exemplo
        # : ----> todos
        # 1:10--> valores de 1 até 10
        # :10---> todos os valores até 10
        # 10 ---> somente valor 10
        print("Separando dados ...")
        dadosTreinamento, dadosTeste, respostasTreinamento, respostasTeste = train_test_split(dados, respostas, test_size=0.05, random_state=0)
        #Rede Neural
        print("Aprendendo ...")
        # verbose= exibir_teste - Max_inter = Maximo de testes, tolerancia de erros
        sefl.classificador = MLPClassifier(verbose=False, max_iter=1000, tol=0.000010)
        # treinar
        sefl.classificador.fit(dadosTreinamento, respostasTreinamento)
        print("Concluído!")

    def testar(self, paciente):
        if self.classificador.predict(paciente.informar()):
            return True
        else:
            return False
