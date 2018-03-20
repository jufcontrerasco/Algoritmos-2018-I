import random
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


def isortSteps(a):
    v = []
    for i in range(len(a)):
        v.append(a[i])

    steps = 0
    for i in range(1,len(v)):
        x = v[i]
        j = i - 1
        while (j > -1) and (v[j] > x):
            v[j + 1] = v[j]
            j = j - 1
            steps = steps + 3
        steps = steps + 1
        v[j + 1] = x
        steps = steps + 4
    steps = steps + 1
    return steps

permAle = []
for i in range(0, 10):
    l = randomPerm(x)
    permAle.append(l)
print("Permutaciones aleatorias: "+str(permAle)+"\n")

sum = 0
avg= 0
for k in range(0,len(permAle)):
    pre = 0
    comp = 0
    swap = 0
    i = 1
    aux = list(permAle[k])
    preguntas =[]
    print("Permutacion de entrada: "+str(aux))
    while i < len(aux):
        d = aux[i]
        j = i-1
        pre = pre+1
        comp = comp+1
        while j > -1 and aux[j] > d:
            aux[j+1] = aux[j]
            swap = swap + 1
            aux[j] = d
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
    print("Numero de pasos: "+str((2*x-1)+3*(sum)))
    print("Numero de pasos, isortSteps: "+str(isortSteps(permAle[k]))+"\n")
    avg = avg + (2*x-1+3*(sum))
    preguntas = []
    sum = 0
print("Numero promedio de pasos: "+str(avg/len(permAle)))


"""for i in range(runs):
    t = isortSteps(randomPerm(n))
    print(t)
    if t < min:
        min = t
    if t > max:
        max = t
    sum = sum + t
print('Theoretical best time, ' + str( 5 * n - 4 ))
print('Theoretical worst time,' + str( (3.0 / 2.0) * n ** 2 + (7.0 / 2.0) * n - 4 ))
print('Theoretical average time,' + str( (3.0 / 4.0) * n ** 2 + (17.0 / 4.0) * n - 4 ))
print('Experimenal best time, ' + str( min ))
print('Experimenal worst time,' + str( max ))
print('Experimenal average time,' + str( sum / runs ))"""