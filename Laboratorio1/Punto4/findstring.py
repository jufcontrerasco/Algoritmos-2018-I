a = input()
b = input()
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)]== sub_string:
            count = count+1
    print(count)
count_substring(a,b)