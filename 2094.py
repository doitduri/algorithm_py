n = int(input())

yearsInfo = []

for i in range(n):
    info = list(map(int, (input().split())))
    yearsInfo.append(info)

m = int(input())

peopleSays = []


def answer(y, x):
    yearsInfo.sort(key=lambda t: t[1])
    print(yearsInfo)

    yIndex = (i for i, j in enumerate(yearsInfo) if j[0] == y)
    xIndex = (i for i, j in enumerate(yearsInfo) if j[0] == x)

    yIndex = int(yIndex)
    xIndex = int(xIndex)
    print(y, yIndex, x, xIndex)

    # 1st condition
    print(xIndex > yIndex)
    # if xIndex > yIndex:
    #     print("1")
    #     return "false"
    #
    # # 2st condition y < z < x
    # for i in range(n):
    #     if yearsInfo[i][1]>yearsInfo[yIndex][1]:
    #         return "false"
    #     print(i)
    return "true"




for i in range(m):
    y, x = map(int, input().split())
    peopleSays.append(answer(y, x))


for i in range(len(peopleSays)):
    print(peopleSays[i])




