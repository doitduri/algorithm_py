words = {}

n = int(input())

for i in range(n) :
    w = str(input())
    words[w] = len(w)

words = dict(sorted(words.items(), key=lambda t: (t[1], t[0])))



for i in words.keys():
    print(i)