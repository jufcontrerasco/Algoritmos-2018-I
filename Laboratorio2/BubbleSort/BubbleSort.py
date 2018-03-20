from itertools import permutations
n = int(input())
permutaciones = list(permutations(range(1,n+1)))
avg = 0
for k in range(0, len(permutaciones)):
    comp = 0
    swap = 0
    pasos = 0
    aux = list(permutaciones[k])
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

print("Numero promedio de pasos: "+str(avg/len(permutaciones)))
