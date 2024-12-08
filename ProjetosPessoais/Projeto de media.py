nome = str(input("Digite o nome do aluno(a): "))
ra = int(input("Digite o Ra Do aluno(a):"))

def lernotas():
  n = float(input("Digite uma nota para o aluno(a): "))
  return n 


def resultado(n1,n2,n3,n4,n5,n6,n7):
  media = (n1+n2+n3+n4+n5+n6+n7)/7
  print("Nota 1: ",n1)
  print("Nota 2: ",n2)
  print("Nota 3: ",n3)
  print("Nota 4: ",n4)
  print("Nota 5: ",n5)
  print("Nota 6: ",n6)
  print("Nota 7: ",n7)
  print("Media: ",media,"Resultado: ",end="")
  if media >= 7:
    print("Aprovado")
  else:
    print("Reprovado")

if ra <= 15:
   print("Ra do aluno: ",ra)
else:
   print ("Ra invalido")

a = lernotas()
b = lernotas()
c = lernotas()
d = lernotas()
e = lernotas()
f = lernotas()
g = lernotas()

resultado(a,b,c,d,e,f,g)

print("Nome do aluno(a):",nome)
print ("Ra do aluno(a):",ra)
#isso é só um teste
#Ass:GBJ
