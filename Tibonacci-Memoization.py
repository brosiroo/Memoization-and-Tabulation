def tibm(x):
    if x in l:
        return l[x]
       
    if x == 0 or x == 1 or x == 2:
        return 0
    elif  x == 3:
        return 1    
    else:
        res = tibm(x-1)+tibm(x-2)+tibm(x-3)
        l[x] = res
    return res

l = {}
x = int(input())
print(tibm(x))