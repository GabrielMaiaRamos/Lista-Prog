#===1===
L = int(input())
T1 = 1
if T1<L:
   print(T1)
T2 = 1
if T2<L:
   print(T2)
while T1+T2 <= L:
   T = T1+T2
   print(T)
   T1 = T2
   T2 = T

#===2===
#a)
Q = int(input("Digite quantos números: "))
S = 0
P = 1
if 1<=Q<=30:
   for c in range(1,Q+1):
      N = int(input())
      S += N
      P *= N
      if c == 1:
         MAIOR = MENOR = N
      else:
         if N>MAIOR:
            MAIOR = N
         elif MENOR>N:
            MENOR = N
MEDIA = S/N
print("Média: {:.2f}\nSoma: {}\nProduto: {}\nMenor: {}\nMaior: {}".format(MEDIA, S, P, MENOR, MAIOR))
      
#b)
N = int(input("Digite qual tabuada: "))
for c in range(1,11):
   print("{} x {} = {}".format(N, c, N*c))

#c)
N = int(input())
R = 1
for c in range(1,51): 
    if c%2 != 0:
        print(R+N)
        R += 4
if c%2 == 0:
   print(R*N)
   R += 4

#d)
for c in range(100,1000):
   c = str(c)
   A, B, C = int(c[0]), int(c[1]), int(c[2])
   if int(c) == (A**3)+(B**3)+(C**3):
      print(c)

#e)
N = int(input("Digite o número: "))
M = 1
for c in range(1, (N//2)+1):
   M *= c
   if M == N:
      print("triangular")
      break
   else:
      print("Não é triangular")

#f)
N = int(input())
S = 0
for c in range(1, N+1):
   for i in range(1,c):
     if i%c == 0:
         S += i
         if S == c:
            print(c)

#g)
T = 0
P1 = 1
P2 = 2
while P1<=P2:
    P1 = 800 * (1.03)**T
    P2 = 2000 * (1.015)**T
    if P1>=P2:
        print("{} anos".format(T))
        break
    T+=1

#h)
L = str(input()).strip().split()
for c in range (0,len(L)-1):
    A = int(L[c])
    B = int(L[c+1])
    if A<B:
        C = True
    elif A>B:
        print("Não está em ordem")
        C = False
        break
if C:
    print("Ordem Crescente")

#========3========
from random import randint
A = 0
E = 0
while A<3:
   X, Y = int(randint(1,100)), int(randint(1,100))
   R = X*Y
   N = int(input("quanto é o poder {} multiplicado pela resistência {} da carta? ".format(X, Y)))
   if N == R:
      A += 1
   elif N != R:
      E += 1
T = A+E
print("Tentativas usadas: {}\nAcertos: {}\nErros: {}".format(T, A, E))

#========4========
N = int(input("Digite o primeiro valor: "))
N2 = int(input("Digite o segundo valor: "))
while N2 != 0:
    R = N%N2
    if R == 0 and N2 != 1:
        print("Números são bros")
        break
    N = N2
    N2 = R

#========5========
L = [2,2,3,3]
W = True
while W:
    N = int(input("Digite quando termos: "))
    for c in range(N):
        if c>=4:
            L.append(2*(L[c-1]+L[c-2])-(L[c-3]*L[c-4]))
        print(L[c])
        if c == N-1:
            P = str(input("Deseja usar o programa novamente? ").strip().lower())
            if P in "nao, não":
                W = False

#========6========
W = True
while W:
    S = 0
    N = int(input("Digite o n: "))
    M = int(input("Digite o m: "))
    for i in range(1, N+1):
        print("i=", i)
        for j in range(1, M+1):
            print("j=", j)
            S += (i**2 * j)/(3**i * (j*3**i + i*3**j))
            print(f"i= {i} e j= {j}, entao S = {S}")
    PERG = input("deseja continuar? ").lower()
    if PERG in "nao, não":
       Q = False

#========7========
from random import randint
V1 = 0
VPC = 0
#CRIO UMA LISTA
L = ["Pedra","Spock","Papel","Lagarto","Tesoura"]
while V1<3 and VPC<3:
    #PEÇO AS ESCOLHAS DE CADA UM
    N = int(input("[0] = Pedra \n[1] = Spock \n[2] = Papel \n[3] = Lagarto \n[4] = Tesoura\nEscolha: "))
    PC = randint(0,4)
    #PARA COMPARAR: Se eu PC escolhe um valor que está 1 ou 2 posições NA FRENTE do que o N escolheu, PC ganha.
    #Logo, crio mais duas variáveis que some 1 e 2 aos valores escolhidos para comparar lá na frete.
    PC1 = PC+1
    PC2 = PC+2
    N1 = N+1
    N2 = N+2
    #Se forem IGUAIS, ninguém ganha
    if PC == N:
        continue
    #Caso N seja 3, quando fizer N2 = N+2, resultará em um valor fora da lista. Mas, como seria uma "lista
    #circular", então, eu forço N2 a virar o primeiro termo.
    if N == 3:
        N2 = 0
    #Caso N seja 4, faço o mesmo que anteriormente, mas nesse caso, N1 e N2 estarão fora da lista. Logo,
    #forço os dois a virarem os valores corretos
    if N == 4:
        N1 = 0
        N2 = 1
    #Faço o mesmo para o PC no dois casos
    if PC == 3:
        PC2 = 0
    if PC == 4:
        PC1 = 0
        PC2 = 1
    #Agora comparo, o valor da posição N, seja o mesmo que o do PC+1 ou PC+2, então N ganha
    if L[N] == L[PC1] or L[N] == L[PC2]:
    #Mesma coisa, mas em caso que o valor da posição PC seja o mesmo que o do N+1 ou N+2, então PC ganha
        V1+=1
    if L[PC] == L[N1] or L[PC] == L[N2]:
        VPC+=1
    #Zero todos os valores que somei 1 ou 2
    PC1=PC2=N1=N2=0