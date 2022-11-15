class CoinChange:
    def NumberofCoins(self, denomination, value):
        dp = [1e9]*(value+1)
        dp[0] = 0
        for val in range(1, value+1, 1):
            for idx in range(0, len(denomination), 1):
                if(denomination[idx] <= val):
                    dp[val] = min(dp[val], 1 + dp[val - denomination[idx]])
        return dp[value]