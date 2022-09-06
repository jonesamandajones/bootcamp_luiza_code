

# 4. Crie um professor de classe com atributos nome, idade e salário, onde
# o salário deve ter um método privado que não pode ser acessado fora
# da classe.
# a. Crie um método para acessar o método privado, onde é passada
# a identificação do usuário se ele pode ou não acessar.

class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
      
    def pede_senha(__get_salario):
        def wrapper(senha, salario):
            senha = input('Senha:    ')
            if senha == 'senha':
                __get_salario(salario)
            else:
                'Acesso não autorizado.'
        return wrapper
    
    @pede_senha    
    def __get_salario(self, salario):    
        self.salario = salario


def main():
    
    nome = input('Informe seu nome:    ')
    idade = input('Informe sua idade:    ')
    salario = (input('Informe seu salário:    ')) 
    professor = Professor(nome, idade, salario)
    salario = Professor.__get_salario(salario)
    print(f'Nome {professor.nome}, idade {professor.idade} anos, seu salário é de R$ {professor.salario}.')

if __name__ == '__main__':
    main()            