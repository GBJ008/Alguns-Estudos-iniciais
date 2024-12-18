a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))

if a <= b and a <= c :
#  A é menor dos Três 
    if b<=c:
# Decide quem é o menor entre b e c 
        print('Ordem Cresente: {}, {}, {}'.format(a,b,c))
    else:
        print('Ordem cresente: {}, {}, {}'.format(a,b,c))
elif b<= a and b <= c:
# B é o menor dos Três 

    if a<=c:
    # decide quem é o menor enre A e o c
        print('Ordem crescente: {}, {}, {}'.format(b,a,c))
else:
    print('Ordem cresencete: {}, {}, {}'.format(b,c,a))

# c é o menor dos Três (opção que sobrou. por isso else)
if a<= b:
    # decide quem é o menor entre a e b
    print('Ordem decrecenste:{}, {}, {}'.format(c,a,b))
else:
    print('Ordem crescente: {}, {}, {}'.format)

    