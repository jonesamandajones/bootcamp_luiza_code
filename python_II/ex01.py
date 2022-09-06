# 1. Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
# classe onde teremos o retorno do documento, o retorno do nome e
# verificação de tipo de pessoa, onde um método irá receber como
# parâmetro “F” ou “N” para trazer fumante ou não fumante.
# Feito isso, crie uma instância e retorne esses valores.

class Pessoa:
    def __init__(self, CPF, nome, idade):
        self.CPF = CPF
        self.nome = nome
        self.idade = idade
       
    def fumante_ou_nao(self, fumante):
        if fumante == 'F' or fumante == 'f':
            self.fumante = 'fumante'
        elif fumante == 'N' or fumante == 'n':
            self.fumante = 'não fumante'

def main():
    CPF = input('Informe seu cpf:   ')
    nome = input('Informe seu nome:    ')
    idade = input('Informe sua idade:    ')
    fumante = (input('Você é fumante? [F/N]    ')) 
    pessoa = Pessoa(CPF, nome, idade)
    pessoa.fumante_ou_nao(fumante)
    print(f'Nome {pessoa.nome}, CPF {pessoa.CPF}, idade {pessoa.idade} anos, {pessoa.fumante}.')


if __name__ == '__main__':
    main()            