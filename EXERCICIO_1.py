class calculadora: #criando a classe
    #definindo funções de cada operação
    def __init__(self, a, b) -> None: #método construtor
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b
    def subtracao(self):
        return self.a - self.b
    def divisao (self):
        return self.a / self.b
    def multiplicacao (self):
        return self.a * self.b
    def exponenciacao (self):
        return self.a ** self.b
    def modulo (self):
        return self.a % self.b
    #fim da definição das funções
    #inicio do programa principal
print("Calculadora. Aluno: Guilherme Lourenço, RU: 3799879") #identificador pessoal
while True: #loop o funcionamento do menu
    try:
        opcao = int(input("Digite a opção desejada:\n1-Somar\n2-Subtrair\n3-Dividir\n4-Multiplicar\n5-Exponenciação\n6-Módulo\n7-Sair"))
        if opcao == 1:
            a = int(input("Digite o primeiro valor"))
            b = int(input("Digite o segundo valor"))
            operacao = calculadora(a,b)
            print(operacao.soma())
        elif opcao == 2:
            a = int(input("Digite o primeiro valor"))
            b = int(input("Digite o segundo valor"))
            operacao = calculadora(a, b)
            print(operacao.subtracao())
        elif opcao == 3:
            a = int(input("Digite o primeiro valor"))
            b = int(input("Digite o segundo valor"))
            operacao = calculadora(a,b)
            print(operacao.divisao())
        elif opcao == 4:
            a = int(input("Digite o primeiro valor"))
            b = int(input("Digite o segundo valor"))
            operacao = calculadora(a,b)
            print(operacao.multiplicacao())
        elif opcao == 5:
            a = int(input("Digite o primeiro valor"))
            b = int(input("Digite o segundo valor"))
            operacao = calculadora(a, b)
            print(operacao.exponenciacao())
        elif opcao == 6:
            a = int(input("Digite o primeiro valor"))
            b = int(input("Digite o segundo valor"))
            operacao = calculadora(a, b)
            print(operacao.modulo())
        elif opcao == 7:
            print("Encerrando a calculadora...")
            break #encerra o loop e fecha o programa
        else:
            print("Digite uma opção válida")
    except ValueError: #tratamento de erro
        print("Você digitou um valor inválido!\nTente novamente.")

