string=list(input("Enter value "))
y=""
for i in range(len(string)):
    if type(string[i])!=int:
        if string[i]==' ':
            y=y+string[i].replace(" ","")
        else:
            y=y+string[i]
    else:
        y=y+str(string[i])
a=list(y)
print(a)
b=[]
for i in y:
    i=int(i)
    b.append(i)
print(b)
print(type(b[1]))