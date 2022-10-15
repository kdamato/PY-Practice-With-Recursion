# Write code for algorithm 2 below

def natural_numbers(x,i):
	#your code here
    if x > i:
        return
    else:
        print(x)
        natural_numbers(x + 1, i)

n = 1
natural_numbers(n,3)
#output: 1 2 3