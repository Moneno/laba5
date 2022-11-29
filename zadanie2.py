import matplotlib.pyplot as plt
import random
n = random.randint(5,100)
a = [random.uniform(0,100) for i in range(int(n))]
m = set()
sr = sum(a)/len(a)
rb = 0
for i in a:
    mi = i*(a.count(i)/len(a))
    m.add(mi)
    rb += (i - sr)**2
srkv = (rb/len(a))**0.5
print(sum(m))
print(srkv)

ni = [i for i in range(len(a))]
k = (n*sum([a[i]*i for i in ni]) - sum(ni)*sum(a))/(n*sum([i**2 for i in ni]) - sum(ni)**2)
b = (sum(a) - k*(sum(ni)))/n

y = [k*i + b for i in ni]

fig, ax = plt.subplots()
ax.plot(ni, y)
ax.scatter(ni,a)
plt.show()