import matplotlib.pyplot as plt

with open('input.txt') as fin:
    data = fin.read().split('\n')

data = [line.split(';') for line in data]
header = data[0]
data = data[1:]
data = [list(map(int, line)) for line in data]

d_open = [[], [], [], []]
d_max = [[], [], [], []]
d_min = [[], [], [], []]
d_close = [[], [], [], []]

for line in data:
    for i in range(4):
        d_open[i].append(line[i * 4])
        d_max[i].append(line[i * 4 + 1])
        d_min[i].append(line[i * 4 + 2])
        d_close[i].append(line[i * 4 + 3])

d = []

for i in range(4):
    d.append(d_open[i])
    d.append(d_min[i])
    d.append(d_max[i])
    d.append(d_close[i])


print(header)

plt.boxplot(d)
plt.xticks([i for i in range(len(header) + 1)], [''] + header)
plt.show()