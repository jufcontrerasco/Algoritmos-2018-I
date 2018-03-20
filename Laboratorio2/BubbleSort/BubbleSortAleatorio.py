import random
from itertools import permutations

x = int(input())
def randomPerm(n):
    v = []
    for i in range( n ):
        v.append( i + 1 )
    for i in range( len( v ) - 1 ):
        j = random.randint( i, len( v ) - 1 )
        aux = v[i]
        v[i] = v[j]
        v[j] = aux
    return v

permAle = []
for i in range(0, 10):
    l = randomPerm(x)
    permAle.append(l)
print("Permutaciones aleatorias: "+str(permAle)+"\n")

avg = 0
for k in range(0, len(permAle)):
    comp = 0
    swap = 0
    pasos = 0
    aux = list(permAle[k])
    preguntas =[]
    print("Permutacion de entrada: "+str(aux))

    l = 1
    while l <len(aux):
        for i in range(0,len(aux)-l):
            x = aux[i]
            y = aux[i + 1]
            comp = comp+1
            if x > y:
                aux[i]=aux[i+1]
                aux[i+1]=x
                swap =swap+1
            print(aux)
        l = l+1
    print("Comparaciones: " + str(comp))
    print("Swaps: " + str(swap))
    pasos = swap+comp
    avg = avg + pasos
    print("Numero de pasos: "+str(pasos)+"\n")

print("Numero promedio de pasos: "+str(avg/len(permAle)))