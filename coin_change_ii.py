class Solution:
    def helper(self, ind, target, dp, coins):
        if ind == 0:
            return 1 if target % coins[ind] == 0 else 0
        
        if dp[ind][target] != -1:
            return dp[ind][target]
        
        notTake = self.helper(ind - 1, target, dp, coins)
        take = 0
        if coins[ind] <= target:
            take = self.helper(ind, target - coins[ind], dp, coins)
        
        dp[ind][target] = notTake + take
        return dp[ind][target]
    
    def change(self, amount, coins):
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        return self.helper(len(coins) - 1, amount, dp, coins)
