#==========1==========
def formar_lista():
    from random import randint
    valores = [randint(1,100) for _ in range(100)]
    return valores

def achar_indice(lista, numero):
    indices = []
    for c in range(len(lista)):
        if lista[c] == numero:
            indices.append(c+1)
    return indices

def main():
    L = formar_lista()
    N = int(input("Digite um valor entre 1,100\n"))
    INDICE = achar_indice(L, N)
    if INDICE:
        print(f"o valor {N} foi encontrado nas posições: {INDICE}")
    else:
        print(f"o valor {N} não foi encontrado")
if __name__ == "__main__":
    main()

#==========2==========
def anotar_clientes():
    from random import randint
    clientes = [randint(1,100) for _ in range(500)]
    return clientes

def promocao(clientes):
    locacao_gratis = []
    locacao_gratis = [(c//10) for c in clientes]
    return locacao_gratis

def main():
    LOC = promocao(anotar_clientes())
    for i in range(len(LOC)):
        print(f"cliente {i+1} =>> {LOC[i]} locações gratuitas")
    print(f"\ntotal de locações gratuitas =>> {sum(LOC)}")

if __name__ == "__main__":
    main()

#==========3==========
def ler_lista(quantidade):
    from random import randint
    lista = [randint(-5,10) for _ in range(quantidade)]
    return lista

def inverter_listaA(listaA):
    listaA_invertida = listaA[::-1]
    return listaA_invertida

def fatorial_da_listaA(listaA):
    lista_fatorial = []
    for c in listaA:
        fatorial_num = c
        for i in range(c-1, 0, -1):
            fatorial_num *= i
        lista_fatorial.append(fatorial_num)
    return lista_fatorial
        
def main():
    A = ler_lista(int(input("Digite quantos termos na lista A: ")))
    INVERSA_A = inverter_listaA(A)
    FATORIAL = fatorial_da_listaA(A)
    print(f"Lista Padrão: {A}\nLista com os Fatoriais de A: {FATORIAL}\nLista inversa: {INVERSA_A}")

if __name__ == "__main__":
    main()

#==========4==========
def formar_lista_com_floats():
    from random import uniform
    lista = []
    for c in range(100):
        lista += list(map(float, "{:.1f}".format(uniform(1,100)).split()))
    return lista

def media_da_lista_sem_usar_sum(lista):
    soma = 0
    for c in lista:
        soma += c
    media = soma/len(lista)
    return media

def identificar_termo_proximo(lista, media):
    for c in lista:
        if c == lista[0]:
            num = abs(media-c)
            termo = c
        else:
            if abs(media-c) < num:
                num = abs(media-c)
                termo = c
    return termo

def main():
    LISTA = formar_lista_com_floats()
    MEDIA = media_da_lista_sem_usar_sum(LISTA)
    TERMO = identificar_termo_proximo(LISTA, MEDIA)
    print(f"Lista = {LISTA}\nMédia = {MEDIA}\nTermo mais próximo da média = {TERMO}")

if __name__ == "__main__":
    main()

#==========5==========
def ler_listas():
    from random import randint
    lista1 = [randint(1,100) for _ in range(int(input()))]
    lista2 = [randint(1,100) for _ in range(int(input()))]
    return lista1, lista2

def intercalar_listas(lista1, lista2):
    lista_interc = []
    for c in range((max(len(lista1),len(lista2)))):
        if c < len(lista1):
            lista_interc.append(lista1[c])
        if c < len(lista2):
            lista_interc.append(lista2[c])
    return lista_interc

def main():
    L1, L2 = ler_listas()
    INTERC = intercalar_listas(L1,L2)
    print(f"Lista 1 = {L1}\nLista 2 = {L2}\nIntersecção das listas = {INTERC}")

if __name__ == "__main__":
    main()

#==========6==========
def candidatos_notas_medias():
    from random import randint
    nomes = []
    notas = []
    medias = []
    for _ in range(int(input())):
        nome = str(input("Digite o nome do candidato: ").split())
        nomes.append(nome)
        notas_individual = [randint(1,10) for _ in range(3)]
        notas.append(notas_individual)
        medias.append(sum(notas_individual)/3)
    return nomes, notas, medias

def main():
    NOME, NOTA, MEDIA = candidatos_notas_medias()
    print("\033[1;33mNOME        NOTAS\033[m")
    for c in range(len(NOME)):
        print(NOME[c], NOTA[c])
    print("\n\033[1;33mNOME     MEDIA\033[m")
    for i in range(len(NOME)):
        print("{} {:.2f}".format(NOME[i], MEDIA[i]))

if __name__ == "__main__":
    main()

#==========7==========
def bobble_sorte(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

agenda = []
for c in range(100):
    N = input("digite um número (ou _sair_ para parar) ")
    if N in "sair, SAIR":
        break
    else:
        agenda.append(int(N))
        agenda = bobble_sorte(agenda)
        print(agenda)