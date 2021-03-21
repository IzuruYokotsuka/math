import matplotlib.pyplot as plt
import math

def cal(x):
    r = []
    l = [1, x[0]] 
    for n in (x + "x")[1:]:
        if n is l[1]:
            l[0] += 1
        else:
            r.extend(l)
            l = [1, n]
    return "".join(map(str,r))

def look_and_say(a1, n):
    s = str(a1)
    r = [str(a1)]
    for i in range(n-1):
        s = cal(s)
        r.append(s)
    return r


n = 20
x = list(range(1, n + 1))
list = [1 ,13, 23, 312, 55555]
for a1 in list:
    s = look_and_say(a1, n)
    plt.plot(x, [len(d) for d in s], label=f'a1={a1}')
    # a = math.log10(int(s[19])) / math.log10(int(s[18]))
    # b = math.log10(int(s[29])) / math.log10(int(s[28]))
    # c = math.log10(int(s[39])) / math.log10(int(s[38]))
    # d = math.log10(int(s[49])) / math.log10(int(s[48]))
    # print(f'a1={a1}', format(a, '.3f'), format(b, '.3f'), format(c, '.3f'), format(d, '.3f'))

plt.yscale('log')
plt.xlim(0, 20)
plt.xticks(x, x)
plt.ylim(0, 100000)
plt.legend()
plt.show()

