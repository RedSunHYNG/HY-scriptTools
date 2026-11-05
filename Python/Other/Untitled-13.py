a = input()
m=len(a)
n=0
x=[]
while n<m:
    b=ord(a[n])
    c=b-3
    if c<97:
        c=c+26
    d=chr(c)
    x.append(d)
    string = ''.join(x)
    n=n+1
print(string)