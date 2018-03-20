from itertools import permutations
n = int(input())
permu = list(permutations(range(1,n+1)))
sum = 0
avg =0
for k in range(0,len(permu)):
    pre = 0
    comp = 0
    swap = 0
    i = 1
    aux = list(permu[k])
    preguntas =[]
    print("Permutacion de entrada: "+str(aux))
    while i < len(aux):
        x = aux[i]
        j = i-1
        pre = pre+1
        comp = comp+1
        while j > -1 and aux[j] > x:
            aux[j+1] = aux[j]
            swap = swap + 1
            aux[j] = x
            j = j-1
            if j >= -1:
                pre= pre+1
            if j >= 0:
                comp= comp+1
        preguntas.append(pre)
        pre = 0
        if len(preguntas) == len(aux)-1:
            print("Numero de preguntas: "+str(preguntas))
        i = i+1
        """print( "Cambio: "+str(aux[:]) )"""
    for i in range(0,len(preguntas)):
        sum = sum + preguntas[i]
    print("Comparaciones: "+str(comp))
    print("Swaps: "+str(swap))
    print ("Lista ordenada: %s" % aux)
    print("Numero de pasos: "+str(2*n-1+3*(sum))+"\n")
    avg = avg+(2*n-1+3*(sum))
    preguntas = []
    sum = 0
print("Numero promedio de pasos: "+str(avg/len(permu)))