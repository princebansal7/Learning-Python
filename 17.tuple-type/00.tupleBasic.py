t = 10,20,30
print(t)

def fun(*t):
    return sum(t)/len(t)
    
t1=(10,20,30,40)
print(fun(*t1))