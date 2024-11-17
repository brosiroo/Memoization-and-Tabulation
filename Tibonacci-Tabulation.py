def tibt(x):
    
        tab = [0]*(x)
        tab[0] = 0
        tab[1] = 0
        tab[2] = 1
        for i in range(3,x):
            tab[i] = tab[i-1] + tab[i-2] + tab[i-3]
           
        return tab[x-1]    



x = int(input())
print(tibt(x))