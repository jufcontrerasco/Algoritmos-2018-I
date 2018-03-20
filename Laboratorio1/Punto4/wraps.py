import textwrap
s = input()
t = int(input())

def wrap(string, tam):
    salida = textwrap.wrap(string,tam)
    for i in range(0,len(salida)):
        print(salida[i])
wrap(s,t)