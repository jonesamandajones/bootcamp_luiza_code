# 23) Neste script você irá ler o nome de 4 alunos e suas notas e determinar qual
# aluno possui a maior nota.


def nota_maior(total):
    maior = total[0][1]
    if total[1][1] > maior:
        maior = total[1][1]
        if total[2][1] > maior:
            maior = total[2][1]
            if total[3][1] > maior:
                maior = total[3][1]
    return maior
 
def aluno(maior, total):
    for n in total:
        if maior in n:
            print(f'O aluno com a maior nota é o {n[0]}.')
    

def main():
       
    aluno1 = [input('Informe o nome do primeiro aluno:   ')]
    aluno1.append(int(input('Informe a nota do primeiro aluno:    ')))
    aluno2 = [input('Informe o nome do segundo aluno:   ')]
    aluno2.append(int(input('Informe a nota do segundo aluno:    ')))
    aluno3 = [input('Informe o nome do terceiro aluno:   ')]
    aluno3.append(int(input('Informe a nota do terceiro aluno:    ')))
    aluno4 = [input('Informe o nome do quarto aluno:   ')]
    aluno4.append(int(input('Informe a nota do quarto aluno:    ')))

    total = [aluno1, aluno2, aluno3, aluno4]
    maior = nota_maior(total)
    aluno(maior, total)    

if __name__ == '__main__':
    main()