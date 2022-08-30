


# 18) Faça um programa que leia a nota de um aluno. Garanta que a nota seja um
# valor inteiro entre zero e 100. Se o valor não estiver neste intervalo, informe que a
# nota é inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso
# contrário, informa que ele foi reprovado.

nota = int(input('Digite sua nota entre 0 e 100:   '))

if nota >= 60 and nota <= 100:
    print('Parabéns, vc foi aprovado!')
elif nota <= 60 and nota >= 0:
    print('Você foi reprovado.')
else:
    print('Você não informou uma nota válida.')   
    
    
