n = input()
d = n.split()
def capitalize(string):
   return string.capitalize()
print(capitalize(d[0]))
for i in range(0,len(d)):
    n = n.replace(d[i],capitalize(d[i]))
print(n)