#Given is a list with spaces, find out the second largest number.
def conv(n,string):
    y=""
    for i in range(n):
        if type(string[i])!=int:
            if string[i]==' ':
                y=y+string[i].replace(" ","")
            else:
                y=y+string[i]
        else:
            y=y+str(string[i])
    intlist=[]
    for i in y:
        i=int(i)
        intlist.append(i)
    return intlist

def runnerup(n,ans):
    ans.sort(reverse=True)
    a=ans[0]
    for b in ans:
        if a==b:
            ans.remove(b)
    y=ans[1:]
    return y[0]
    

string=["2"," ","3",' ',"6",' ',"6"," ","5"]
n=len(string)
ans=conv(n,string)
print(runnerup(n,ans))
#arr = map(int, input().split())
#This function is used to clear up the space in between and convert the givne list into integer
# replacing which by algorithm took me 4 hours.
#-------------------------------

def runnerup(n,abc):
    abc.sort(reverse=True)
    a=abc[0]
    abc=abc[1:]
    while a in abc:
        abc.remove(abc[0])
    y=abc[:]
    return y[0]


#int(input())
arr = [8,7,8,5,4]#map(int, input().split())
n = len(arr)
abc=list(arr)
print(runnerup(n,abc))
    