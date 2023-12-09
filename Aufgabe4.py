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
    q = 2
    while n > 1:
        if n%q == 0:
            res.append(q)
            n = n//q
            q = 2
        else:
            q += 1
        if (q == n):
            break
    return res
