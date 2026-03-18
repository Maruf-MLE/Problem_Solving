import string
width = 17
height = 9
n = 5
string = string.ascii_lowercase
print(string)
print(string[n:n+2])
nf = n-1
lin = string[nf]
line = ''


for i in range(4):
    
    
    
    print(lin.center(width,'-'))
   
    
    lin += string[n-2]

    # print(lin)
    lin += lin[:-1][::-1]
    n -= 1
    

print(line)
print(string[n-1:n])