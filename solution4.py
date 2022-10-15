# Write code for algorithm 4 below

def power(num ,exp):
    if exp==0:
        return 1
    else: 
        return num*power(num,exp-1)

a=2
b=4

print(power(a,b))