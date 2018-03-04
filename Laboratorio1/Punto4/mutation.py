a = input()
b = input()
c, d = b.split(" ")
pos = int(c)

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    print(string)

mutate_string(a,pos,d)