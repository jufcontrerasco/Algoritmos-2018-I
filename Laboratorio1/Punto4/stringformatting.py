numero = int(input())

def transfor(numb):
    for i in range(1,numb+1):
        binar = str(bin(i))
        octal = str(oct(i))
        hexa = str(hex(i)).upper()
        decim = str(i)
        f = len(bin(numb))-2
        print(decim.rjust(f),octal[2:].rjust(f),hexa[2:].rjust(f),binar[2:].rjust(f))

transfor(numero)