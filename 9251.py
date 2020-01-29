A= [x for x in input()]
B= str(input())

dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]


for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        dp[i][j]=max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + (A[i-1] == B[j-1]))


print(dp[len(A)][len(B)])