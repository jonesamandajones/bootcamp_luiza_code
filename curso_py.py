#função PRINT

print('coisas aleatórias que vão ser printadas')
print('e aqui eu posso escrever qualquer coisa q vai ser entendida como uma string')
# escrever python3 e nome do arquivo no terminal pra aparecer os rolês
# se eu quiser pular uma linha posso usar o \n
print('eu vou pular uma linha \n')
print('e agora eu printo isso em duas linhas abaixo')

# função INPUT e VARIÁVEL

resposta = input('Diz alguma coisa aí?')

#variável é um post-it :)

print(resposta)

exemplo = 'variável aleatória'
print(f'assim eu consigo chamar qualquer variável colocando ela entre chaves >{exemplo}<')

#del é um comando existente

#ferramenta legal chamada REPL q é basicamente um loop, daí usa o comando python3 -1 e nome do arquivo no terminal (ctrl+d pra sair depois)
# sempre q tiver '>>>' é pq tá no 'shell' q é basicamente esse REPL, ou o -i... o.O
#assim eu consigo chamar qualquer valor/variável de dentro do arquivo pra testar o resultado
#se dentro dessa ferramenta eu usar o comando type(nome de um objeto válido) ele me diz q tipo/classe de objeto ele é (int, str etc.)
 #posso tbm usar print(type(nome do objeto)) no arquivo q ele vai printar no terminal o resultado
 
print(type(exemplo))

#comando DIR 
#pode ser usado pra listar as possibilidades de um objeto. Os métodos de executar ações

dir(exemplo)
 
 
2 + 2
2 ** 2
 
 
 # BOOLEANOS (conectivos lógicos)
 # true() false() >, <, ==, !=, <=, >=, 
 # and> posso usar umma comparação booleana e somar a outra com <and> e tornar toda a expressão um booleano (os dois são reais?)
 # or> uso duas comparações booleanas entre <or> e saber se toda a expressão é true em uma das comparações (ou um ou outro é real?) 
 # not> iniciar uma expressão com <not> só resulta em true se a expressão for falsa. (esses dados aqui são falsos?)
 #
 # IF, ELIF, ELSE (estruturas de decisão)
 #IF> somente se a afirmação for true ação acontece
 #ELIF> se o if for negativo, e a afirmação for true a ação acontece
 #ELSE> se nenhuma das anteriores funcionou, a ação acontece
 #ações sempre ficam identadas
 #   Algumas condições SEMPRE vão ser falsas:
 #    => 0, none, false, ou uma string vazia
 #
#situação = input("Hoje eu acordei bem?")
#if situação == 'sim':
#    print('AEEEE KRAI!')
#elif situação == 'não':
#    print('Quem nunca!?')
#else: 
#    print('Num intindi')

#STRINGS e métodos
texto = """ assim eu consigo escrever um puta texto
mesmo trocando de linhas

pq assim eu torno um texto em uma string"""

string_exemplo = 'Amanda Jones'

print('qualquer coisa' * 30)

print(string_exemplo.count('a'))
print(string_exemplo.replace('Jones', 'Oliveira'))
print(string_exemplo.index('Jones'))
print(string_exemplo.partition(' '))
print(string_exemplo.lower())
print(string_exemplo.split(' '))
print(string_exemplo.find('exemplo'))


####### LAÇOS DE REPETIÇÃO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> WHILE





# ctrl + ; comenta seleção

# COLEÇÕES
# a = [1, 2, 3, 4]

 