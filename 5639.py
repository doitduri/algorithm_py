def post(e):
    if e == '': return
    post(d[e][0])
    post(d[e][1])
    print
    e


e = []
while True:
    try:
        e.append(input())
    except EOFError:
        break
d = {e[0]: ['', '']}
for element in e[1:]:
    c = e[0]
    while True:
        if element < c:
            if d[c][0] == '':
                d[c][0] = element
                d[element] = ['', '']
                break
            else:
                c = d[c][0]
        elif element > c:
            if d[c][1] == '':
                d[c][1] = element
                d[element] = ['', '']
                break
            else:
                c = d[c][1]
post(e[0])