#importando bibliotecas necessárias
import plotly.express as px
import numpy as np
import pandas as pd

class equacao: #criando a classe
    def __init__(self, a, b, c) -> None: #método construtor
        self.a = a
        self.b = b
        self.c = c
    def operacaox1(self):
        x = 5
        y = ((self.a * x) + (self.b * x)) - self.c
        return y
    def operacaox2(self):
        x = 7
        y = ((self.a * x) + (self.b * x)) - self.c
        return y
    def operacaox3(self):
        x = 9
        y = ((self.a * x) + (self.b * x)) - self.c
        return y
#programa prinicpal
operacao = equacao(8,7,9) #criando variável a partir da classe "equacao" tendo como parâmetro os três últimos dígitos do meu RU
#criando vetor de cada resultado das operações usando NumPy
vetor_x1 = np.array([operacao.operacaox1()])
vetor_x2 = np.array([operacao.operacaox2()])
vetor_x3 = np.array([operacao.operacaox3()])
#criando arquivo de texto com os vetores usando NumPy
np.savetxt('x1_resultado.txt', vetor_x1, fmt='%f', delimiter=';')
np.savetxt('x2_resultado.txt', vetor_x2, fmt='%f', delimiter=';')
np.savetxt('x3_resultado.txt', vetor_x3, fmt='%f', delimiter=';')
#carregando arquivo de texto com os vetores usando NumPy
array_x1 = np.loadtxt('x1_resultado.txt', dtype = np.float64, delimiter=';')
array_x2 = np.loadtxt('x2_resultado.txt', dtype = np.float64, delimiter=';')
array_x3 = np.loadtxt('x3_resultado.txt', dtype = np.float64, delimiter=';')

array_x123 = np.vstack([array_x1, array_x2, array_x3]) #juntando os valores dos outros três arrays em uma única variável para plotar o gráfico
print(array_x123)
fig = px.line(array_x123) #plotando gráfico do tipo linha(line)
fig.update_layout(title = 'Gráfico', xaxis_title = 'x', yaxis_title = 'f(x)') #renomeando o gráfico, eixo x e eixo y
fig.update_traces(name = 'Função Linear', line = dict(color = "red"), mode = 'lines+markers') #legendando gráfico, alterando a cor e adicionando marcadores
fig.show()