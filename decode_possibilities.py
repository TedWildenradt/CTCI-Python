def decode(s):
    if not s or s == '0':
        return 0
    dp = [1] + [0] * len(s)
    for i in range(1,len(s)+1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if i > 1 and '09' < s[i-2] + s[i-1] <= '26':
            dp[i] += dp[i-2]
    return dp[-1]

decode('226')