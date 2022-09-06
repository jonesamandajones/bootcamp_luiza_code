
# 3. Escreva uma classe “PessoaJurica” e herde Pessoa, agora
# modificando o comportamento, retorne o cnpj. Crie uma instância e
# acesse os dados

from ex01 import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, CPF, nome, idade):
        super().__init__(CPF, nome, idade)  
        
    def juridica(self, CPF):
        if len(CPF) == 14:
            return f'{self.nome} é pessoa jurídica.'
        
    
def main():
    CPF = (input('Informe seu cpf:   '))
    nome = input('Informe seu nome:    ')
    idade = input('Informe sua idade:    ')
    fumante = (input('Você é fumante? [F/N]    ')) 
    
    pessoa = PessoaJuridica(CPF, nome, idade)
    pessoa.fumante_ou_nao(fumante)
       
    print(f'Nome {pessoa.nome}, identificação {pessoa.CPF}, idade de {pessoa.idade} anos. {pessoa.juridica(CPF)}')

if __name__ == '__main__':
    main()  