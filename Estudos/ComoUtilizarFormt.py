a = input('Digite ')
print('sei lá o que você Digitou {:)>20}'.format(a))
# esse é o exemplo de como colocar caracteres, na informção que deseja, podemos usar também outras seta para por o nome na direção que deseja
# (>)caracteres a esquerda
# (<)Caracteres a direita
# (^)caracteres centralizados
# é possivel usar com números também 
n1 = int(input('valor1: '))
n2 = int(input('valor2: '))
r = n1*n2
print('O Resultado é {:.3f}'.format(r))
# Utilizando esse formato de formate, você consegue selecionar o quantas casa depois da virgula você deseja que apareça
# caso queira que ele não quebre a linha do print você add end=' ' assim ele não vai quebrar a linha do dois print caso add algun caracter dentro do parentese ele será add no termino da linha
# caso queira adicionar quebra de linha e manda o conteúdo para linha de baixo só add(\n) assim a linha será mandada para baixo
# outra forma de usar o format é colocando o %.1f dentro das aspas e do lado de fora por % e a varáivel que deseja, mas isso só funciona para diminuiro os números depois da virgula 
a = int(input('Digite um valor'))
b = int(input('Digite um segundo valor'))
if b == 0 :
  print('Valor indivisivel')
else:
  r = a / b
  print('Resultado: R = %.3f' % r)