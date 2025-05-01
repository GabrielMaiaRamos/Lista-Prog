# ========1========= 
# a) V 
# b) V 
# c) V 
# d) F 
# e) F 
# f) F 
# g) V 
# h) F 
# i) F 
# j) F 

# ========2========

# print(2+2*2**(3*2)/0.5)  
# I) (3*2) = 6  
# II) 2**6 = 64  
# III) 2*64 = 128  
# IV) 128/0.5 = 256  
# V) 2+256 = 258  
# Resultado: True 

# print(not 2 + 0.5 < 3 or 2 + 2 * 0.5 >= 3 and True)  
# I) 2*0.5 = 1  
# II) 
# 2+0.5 = 2.5 
# 2+1 = 3  
# III) 
# 2.5<3 = True
# 3>=3 = True
# temos:  
# print(not True or True and True)  
# IV) not True = False  
# V) True and True = True  
# VI) False or True = True  
# Resultado: True 

# ========3=========

#a) Área do cubo  
A = float(input("Digite a Aresta: "))  
print(6*A**2)

#b) 
A = int(input()) 
B = int(input()) 
C = int(input()) 
S = A+B+C  
M = (S)/3  
P = A*B*C  
print("Média: {:.2f}\nSoma:{}\nProduto:{}\nMenor Valor:{}\nMaior Valor:{}".format(M, S, P, min(A,B,C), max(A,B,C))) 

#c)  
C = str(input("Digite a cor: ")).strip().lower()  
if C == "verde":  
    V = 10  
elif C == "azul":  
    V = 20  
elif C == "amarelo":  
    V = 30  
elif C == "vermelho":  
    V = 40  
print("R$ {:.2f}".format(V)) 

#d)  
A = int(input())  
B = int(input())  
C = int(input())  
if A==B==C:  
    print("0")  
elif A==B:  
    print(A+C)  
elif A==C:  
    print(A+B)  
elif B==C:  
    print(A+C)  
else:  
    print(A+B+C)

#e)  
A = int(input())  
B = int(input())  
C = int(input())  
if A+B==C or A+C==B or B+C==A:  
    print("soma")  
elif A*B==C or A*C==B or B*C==A:  
    print("multi")  
elif (A+B+C)%2 == 0:  
    print("par")  
elif (A+B+C)%2 != 0:  
    print("impar")  

#f)  
A = int(input())  
B = int(input())  
C = int(input())  
if A+B>C and A+C>B and B+C>A and A>0 and B>0 and C>0:  
    print("Podemos formar um triângulo!")  
    if A==B==C:  
        print("Esse triângulo é equilátero")  
    elif A==B!=C or A==C!=B or B==C!=A:  
        print("Esse triângulo é isósceles")  
    elif A!=B!=C:  
        print("Esse triângulo é escaleno")  
else:  
    print("Não podemos formar um triângulo!")

#g)  
N = int(input())  
M = [100, 50, 25, 15, 1]  
for c in M:  
    Q = N//c  
    print("{} moedas de {:.2f} real".format(Q, c))  
    N %= c