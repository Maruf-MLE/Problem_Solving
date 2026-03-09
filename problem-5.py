c = input()
n = len(c)
result = ''

for x in range(n):

    if c[x].isupper() == True:
        result += c[x].lower()
        
    elif c[x].islower() == True:
        result += c[x].upper()
        
    else:
        result += c[x]

print(result)
