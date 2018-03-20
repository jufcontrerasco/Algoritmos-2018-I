n = int(input())
lista = map(int, input().split())
t = tuple(lista)
print(hash(t))
