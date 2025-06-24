#==========1==========
def soma(x,y):
    if y == 0:
        return x
    else:
        return soma(x,y-1) + 1

def subtracao(x,y):
    if y == 0:
        return x
    else:
        return subtracao(x,y-1) - 1

def multiplica(x,y):
    if y == 0 or x == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x+multiplica(x,y-1)

def divide(x,y):
    if x < y:
        return 0
    else:
        return divide(x-y,y) + 1

def interface_calculadora():
    perg = input("Deseja: soma, subtração, multiplicação ou divisão?\n").lower()
    x, y = map(int, input("digite os dois valores: ").split())
    if perg == "soma":
        print(soma(x,y))
    elif perg in "subtracao, subtracão, subtração, subtraçao":
        print(subtracao(x,y))
    elif perg in "multiplicacao, multiplicacão, multiplicaçao, multiplicação":
        print(multiplica(x,y))
    elif perg in "divisao, divisão":
        print(divide(x,y))
    else:
        print("não há essa opção..")

if __name__ == "__main__":
    interface_calculadora()

#==========2==========
def maior_sequencia(L):
    maior = 1
    count = 1
    for c in range(len(L)-1):
        if L[c]<L[c+1]:
            count+=1
            if count > maior:
                maior = count
        else:
            count = 1
    return maior

def main():
    L = list(map(int, input("Digite a lista de termos:\n").split()))
    print(maior_sequencia(L))

if __name__ == "__main__":
    main()

#==========3==========
def ler_lista():
    from random import randint
    L = [randint(-50,50) for c in range(20)]
    return L

def substituir_lista(lista):
    for c in range(len(lista)):
        if lista[c]<0:
            lista[c] = 0
        elif 0<=lista[c]<10:
            lista[c] = 1
        elif lista[c]>10:
            lista[c] = 2
    return lista

def main():
    LISTA = ler_lista()
    print(f"Lista originial = {LISTA}\nLista substituida = {substituir_lista(LISTA)}")

if __name__ == "__main__":
    main()

#==========4==========
def soma_total(n, m):
    soma = 0
    if n == 2:
        return n/m
    for c in range(2, n+1):
        soma += (c)/((2*(c-1))+1)
    return soma

def main():
    n = m = -1
    while True:
        n, m = map(int, input("Digite n,m (ambos positivos) \n").split())
        if n<0 or m<0:
            print("erro\n")
        else:
            print(f"{soma_total(n, m):.2f}")
            break
if __name__ == "__main__":
    main()

#==========5==========
def ler_lista(n):
    from random import randint
    lista = [randint(0,20) for c in range(n)]
    print(lista)
    return lista

def menor_indice(lista, n):
    k = int(input("\nDigite o índice k: "))
    num = lista[k]
    indice = i= 0
    print(f"lista de k ate o final = {lista[k:n]}")
    for c in range(k, n-1):
        i += 1
        if lista[c] < num:
            num = lista[c]
            indice = i+k-1
    return num, indice

def main():
    n = int(input("Digite o tamanho da lista: "))
    L = ler_lista(n)
    elemento, indice = menor_indice(L, n)
    print(f"\nindice = {indice}\nEquivale ao elemento: {elemento}")

if __name__ == "__main__":
    main()

#==========6==========
def numeros_tribonacci(n):
    L = [1,1,2]
    for c in range(3, n):
        L.append(L[c-3]+L[c-2]+L[c-1])
    return L[:n]

def main():
    print(numeros_tribonacci(int(input("Quantos termos de Tribonacci? "))))

if __name__ == "__main__":
    main()

#==========7==========
def eh_palindromo(s, inicio, fim):
    if inicio > fim-1: #se ja verifiquei letra a letra, retorna TRUE
        return True
    
    if s[inicio] == s[fim-1]: #se a letra inicial é igual a final, continuo vendo letra a letra
        return eh_palindromo(s, inicio+1, fim-1) #avanço 1 no inicio e reduzo 1 no final
    else: return False #se alguma letra for diferente da outra, é falso

def main():
    s = input()
    print(eh_palindromo(s, 0, len(s)))

if __name__ == "__main__":
    main()

#==========8==========
def soma_bignum(s1, s2, i,vaium):

    while len(s1) != len(s2): #adiciono 0 caso os termos não tenham o mesmo comprimento
        if len(s1) > len(s2):
            s2 += "0"
        else:
            s1 += "0"

    soma = (int(s1[i])+int(s2[i])+vaium) #faço a soma dos primeiros i termos com o "vaium"

#verifico o caso especifico de quando os numeros tem comprimento = 1 e a soma é maior que 10, pois é só inverter
    if len(s1) == 1 and soma>= 10: 
        return str(soma)[1]+str(soma)[0]

    if soma >= 10 and i != len(s1)-1: #se a soma for maior que 10 e NAO estivermos no ULTIMO termo, então:
        soma -= 10 #reduzo o valor em 10 para passar o "1" para o vaium
        vaium = 1
    else:
        vaium = 0
#por que ver se é o ultimo termo para "jogar para o vaium"?
#por que se for o ultmo termo, nao usaremos o "vaium", apenas colocaremos a soma os dois termos no final do numero.

    if i == len(s1)-1: #se eu estiver no ULTIMO termo, retorno a soma
        return soma
 
    return str(soma) + str(soma_bignum(s1,s2,i+1, vaium))

def main():
    s1, s2 = input("Digite os valores: ").split()
    print(soma_bignum(s1, s2, 0, 0))

if __name__ == "__main__":
    main()

#==========9==========
#a)
# irá converter todo elemento do input em inteiro

#b)
def media(a, b, c):
    return float(str((a+b+c)/3)[:5])

#c)
def lista_aleatoria():
    from random import randint
    L = [randint(0,10) for _ in range(10)]
    print(f"Lista Original = {L}")
    return L

def suavizar(media, lista):
    lista_suavizada = [lista[0]]
    for c in range(len(lista)-2):
        lista_suavizada.append(media(lista[c], lista[c+1], lista[c+2]))
    lista_suavizada += lista[-1:]
    return lista_suavizada

print(f"Lista Suavizada = {suavizar(media, lista_aleatoria())}")