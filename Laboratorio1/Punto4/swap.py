a = input()
def swap(str):
    lista = list(str)
    for i in range(0, len(str)):
        if 'a'<=lista[i]<='z':
            lista[i] = lista[i].upper()
        if 'A'<=str[i]<='Z':
            lista[i] = lista[i].lower()
    str = "".join(lista)
    print(str)
swap(a)