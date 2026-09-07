class Solution:
    def count(self, coins: list[int], sum: int) -> int:
        # code here
        dp=[[0 for c in range(sum+1)] for r in range(len(coins)+1)]
        s=sum
        m=len(coins)
        def solve(coins,m,s):
            for i in range(m+1):
                dp[i][0]=1
                
            for i in range(1, m+1):
                for j in range(1, s+1):
                    
                    dp[i][j]=dp[i-1][j]
                    if j>=coins[i-1]:
                        dp[i][j]=dp[i][j]+dp[i][j-coins[i-1]]
                        
            return dp[m][s]
            
        return solve(coins,m,s)
        
        """
        class Solution:
            def count(self, coins: list[int], sum: int) -> int:

                dp = [[None for c in range(sum + 1)]
                      for r in range(len(coins) + 1)]

                def solve(m, s):

                    if s == 0:
                        return 1

                    if m == 0:
                        return 0

                    if dp[m][s] is not None:
                        return dp[m][s]

                    if coins[m - 1] > s:
                        dp[m][s] = solve(m - 1, s)
                    else:
                        dp[m][s] = solve(m - 1, s) + solve(m, s - coins[m - 1])

                    return dp[m][s]

                return solve(len(coins), sum)
        """