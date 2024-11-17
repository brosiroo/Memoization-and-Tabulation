# factorial using memoization
def facto(x):
    if x in cc:
        return cc[x]
    
    elif x <= 1:
        return 1
    else:
        res = facto(x-1)* x  
        cc[x] = res
        return cc[x]
cc ={}

x = int(input())
print(facto(x))