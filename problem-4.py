n,x = map(int,input().split())
l = []
for i in range(x):
    score = list(map(int,input().split()))
    l.append(score)

print(l[0])

for mark in zip(*l):
    print(sun(mark) / len(mark))
