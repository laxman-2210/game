import random
def check(comp,user):
    if comp==user:
        return 0
    if comp ==0 and user==1:
        return -1
    if comp == 1 and user ==2:
        return -1
    if comp==2 and user ==0:
        return -1
    return 1
comp = random.randint(0,2)
user =int(input(  "0 for Scissor  ,1 for  Paper , 2 for Rock\n "))

score = check(comp,user)

print("you:",user)
print("computer:",comp)
if score==0:
    print("Its Draw")
elif score==1: 
    print("You Won")
else:
    print("You LOse")