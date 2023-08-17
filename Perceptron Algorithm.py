İnputs=[int(x) for x in input("Enter the input values").split()]
weights=[int(w) for w in input("Enter the weight values").split()]
treshold=int(input("Enter the treshold"))
def step(weighted_sum):
    if weighted_sum>treshold:
        return 1
    else:
        return 0
def perceptron():
    weighted_sum=0
    for x,w in zip(İnputs,weights)  :
        weighted_sum+=x*w
    return step(weighted_sum)  
output= perceptron()
print("The result is: ", output)            
