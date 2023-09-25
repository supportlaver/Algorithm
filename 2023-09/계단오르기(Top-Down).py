def DFS(len):
    if dp[len] != 0:
        return dp[len]
    if len == 1 or len == 2:
        return len
    else:
        dp[len] = DFS(len-1) + DFS(len-2)
        return dp[len]
    
if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    DFS(n)
    print(dp[n])