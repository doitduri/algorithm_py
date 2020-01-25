from operator import itemgetter, attrgetter

n = int(input())

member = []

for i in range(n):
    info = (input().split(" "))
    info[0] = int(info[0])
    info[1]=str(info[1])
    member.append(tuple(info))

member.sort(key=lambda t: (t[0]))


for m in member:
    print(m[0], m[1])

