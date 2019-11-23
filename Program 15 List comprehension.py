
#LIst comprehenion
n=int(input("Enter rows:-"))
m=int(input("Enter columns:-"))
res=([[4 for i in range(n)] for j in range(m)])
print(res)
res2=([[0 for i in range(n)]*m])
print(res2)