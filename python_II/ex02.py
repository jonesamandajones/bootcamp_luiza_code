# 2. Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método
# exclusivo para a classe e acesse-o
from ex01 import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome, idade):
        super().__init__(CPF, nome, idade)       

    def fumar(self):
        return f'{self.nome} vai para a área de {self.fumante}.'
    
def main():
    CPF = (input('Informe seu cpf:   '))
    nome = input('Informe seu nome:    ')
    idade = input('Informe sua idade:    ')
    fumante = (input('Você é fumante? [F/N]    ')) 
    
    pessoa = PessoaFisica(CPF, nome, idade)
    pessoa.fumante_ou_nao(fumante)
       
    print(f'Nome {pessoa.nome}, CPF {pessoa.CPF}, idade {pessoa.idade} anos. {pessoa.fumar()}')

if __name__ == '__main__':
    main()  