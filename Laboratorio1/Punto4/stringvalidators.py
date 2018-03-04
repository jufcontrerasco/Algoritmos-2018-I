stri = input()
def validator(string):
    list = [False,False,False,False,False]
    for i in range(0, len(string)):
        if string[i].isalnum():
            list[0]= True
        if string[i].isalpha() == True:
            list[1]= True
        if string[i].isdigit() == True:
            list[2]= True
        if string[i].islower() == True:
            list[3]= True
        if string[i].isupper() == True:
            list[4]= True

    for j in range(0,5):
        print(list[j])
validator(stri)
