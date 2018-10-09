
def g(N,k):
    x = [5000]
    for n in x:
        x.append(1.06*n - k)
        if len(x)>20:
            break
    return x
print(g(N=2000, 400))