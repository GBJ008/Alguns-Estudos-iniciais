#Execício 1 = Escreva um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles
 
numeroUm = float(input('insira o primeiro valor: '))

numeroDois = float(input('insira o segundo valor: '))

calculoMais = numeroUm + numeroDois

calculoMenos= numeroUm - numeroDois

# calculoDivisão = numeroUm / numeroDois

calculoMultiplicação = numeroUm * numeroDois

if numeroDois != 0:
    calculoDivisao = numeroUm / numeroDois
    print('Seu calculo de Dicisão é: ',calculoDivisao)
else:
    print('o Número não pode ser divisivel por 0  ')

print('O seu calculo da Soma é: {} \n Seu calculo da Subtração é: {} \n Seu calculo da Multilicação {}. '
        .format(calculoMais,calculoMenos,calculoMultiplicação))



# Ass:GBJ008
