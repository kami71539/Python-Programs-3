
#ans=(lamba z:z*4)
#Lambda is used to write functions in shorthand
#print(ans(7))
items=[1,2,3,4]
squared=list(map(lambda x:x**2,items))
print(squared)

integers=range(-5,5)
positive_num=list(filter(lambda x:x>0,integers))
print(positive_num)
#Filter is used to filter out and keep only the items which satisfy the requirement.
number=[1,2,3,4]
#ans=reduce((lambda x,y:x*y),number)
#print(ans)
def print_users(user, *users):
    print("First user arg: ",user)
    for user in users:
        print("User is from the argument ",user)
print_users("Admin","Ceo","Project Manager","Intern","Trainee","Associate")

def myfunction(arg1, arg2, arg3, *args, **kwargs):
    print('First normal argument: ', arg1)
    print('First second argument: ', arg2)
    print('First third argument: ', arg3)
    print('First fifth argument: ', kwargs)
myfunction=(1,2,3,4,5,6,7, name='Mehek',country='India', age 22)

        
