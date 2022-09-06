

# 4. Crie um professor de classe com atributos nome, idade e salário, onde
# o salário deve ter um método privado que não pode ser acessado fora
# da classe.
# a. Crie um método para acessar o método privado, onde é passada
# a identificação do usuário se ele pode ou não acessar.

class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.salario = 'Acesso não autorizado'
      
    def pede_senha(_get_salario):
        def wrapper(*args, **kwargs):
            senha = input('Senha:    ')
            if senha == 'senha':
                _get_salario(*args, **kwargs)
            else:
                print('Senha incorreta.')
        return wrapper
    
    @pede_senha
    def _get_salario(self, salario):    
        self.salario = salario


def main():
    
    nome = input('Informe seu nome:    ')
    idade = input('Informe sua idade:    ')
    salario = (input('Informe seu salário:    ')) 
    professor = Professor(nome, idade)
    salario = professor._get_salario(salario)
    
    print(f'Nome {professor.nome}, idade {professor.idade} anos, seu salário é de R$ {professor.salario}.')

if __name__ == '__main__':
    main()            