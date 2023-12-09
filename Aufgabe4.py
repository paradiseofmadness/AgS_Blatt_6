# a)
def sieb_des_eratosthenes(n):
    res = [i for i in range(2, n+1)]
    for i in res:
        for k in range(i+i, n+1, i):
            if k in res:
                res.remove(k)
    return res

# b)
def prim_faktorisierung(n):
    res = []
    f = 2
    while n > 1:
        if n%f == 0:
            res.append(f)
            n = n//f
            f = 2
        else:
            f += 1
        if (f > n):
            break
    return res
