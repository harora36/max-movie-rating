def maximize_ratings(ratings):
    n = len(ratings)
    dp = [float('-inf') for i in range(n)]
    if n == 0:
        return float('-inf')
    for i in range(n):
        if i == 0:
            dp[i] = ratings[i]
        elif i == 1:
            dp[i] = max(dp[0] + ratings[1], ratings[1])
        elif i >= 2:
            dp[i] = max(dp[i-1] + ratings[i], dp[i-2] + ratings[i])
    return max(dp[n-1], dp[n-2])
