# fibonaci using memoization
def fibo(x):
    if x in m:
        return m[x]
    if x <=1:
        return x
    else:
        res = fibo(x-1) +fibo(x-2)
        m[x] = res
    return m[x]
m = {}
x = int(input())
print(fibo(x))
