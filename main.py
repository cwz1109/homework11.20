# Ask for a number to calculate
x=int(input("Give me a number:"))
# define the function to show: F(x)=x*F(x-1)
def F(x):
    if x==1 or x==0:
        return x
    elif x<0:
        print("NO, IT IS Negative")
    else:
        return x*F(x-1)

print("The answer is",F(x))

quit()






