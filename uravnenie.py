import math
def too (a, b, c):
    if(b*b-4*a*c>0):
        print((-b+math.sqrt(b*b-4*a*c))/(2*a))
        print("    ")
        print((-b-math.sqrt(b*b-4*a*c))/(2*a))
    elif(b*b-4*a*c==0):
         print((-b)/(2*a))
    else:
        print("NO")
a=int(input())
b=int(input())
c=int(input())
print(too(a, b, c))





