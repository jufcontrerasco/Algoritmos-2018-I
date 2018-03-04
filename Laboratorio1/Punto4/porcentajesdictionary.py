n = int(input())
dicc = {}
for i in range(0,n):
    datos = input().split()
    sum = 0
    for j in range(1,len(datos)):
        sum = sum+float(datos[j])
    prom = sum /(len(datos)-1)
    dicc["promedio" + datos[0]] = prom
    dicc[datos[0]] = datos[0]
salida = input()
print("{0:.2f}".format(dicc["promedio"+salida]))