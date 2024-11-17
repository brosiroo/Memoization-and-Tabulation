# factorial using tabulaition
def facto2(y):
     if y <=1:
        return y
     tab = [1] * (y+1)
     tab[0]= 1
     tab[1] = 1
     for i in range(2,y+1):
      tab[i] = tab[i-1]*i
     return tab[y] 

x = int(input())
print(facto2(x))