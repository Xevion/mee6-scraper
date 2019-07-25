from matplotlib import pyplot as plt
import pprint

def levelXP(n):
    return (5 * (n ** 2)) + (50 * n) + (100)

def additiveXP(n):
    return sum([levelXP(x) for x in range(0, n)])

x_values = [x for x in range(0,100)]
y_values = [additiveXP(y) for y in range(0, 100)]

pp = pprint.PrettyPrinter()
pp.pprint(x_values)
pp.pprint(y_values)

def notation(n):
    n = int(n)
    qu = 10**18;q = 10**15;t = 10**12;b = 10**9;m = 10**6;k = 10**3
    if n < k:
        return str(n)
    elif n >= qu:
        n = round(n / qu, 1)
        return str(n) + " qu"
    elif n >= q:
        n = round(n / q, 1)
        return str(n) + " q"
    elif n >= t:
        n = round(n / t, 1)
        return str(n) + " t"
    elif n >= b:
        n = round(n / b, 1)
        return str(n) + " b"
    elif n >= m:
        n = round(n / m, 1)
        return str(n) + " m"
    elif n >= k:
        n = round(n / k, 1)
        return str(n) + " k"

with plt.xkcd():
    plt.plot(x_values, y_values)
    for i, txt in enumerate(y_values):
        if i % 10 == 0:
            plt.annotate(notation(txt), (x_values[i], y_values[i]))
    plt.show()