class Solution:
    def countWays(self, n: int) -> int:
        # code here
        dp=[None]*100
        def solve(n):
            if n==0:
                return 1
            if n<0:
                return 0
            if dp[n]!=None:
                return dp[n]
            dp[n] = solve(n-1) + solve(n-2)
            return dp[n]
        return solve(n)
        """
        if n==0:
            return 1
        if n<0:
            return 0
        return self.countWays(n-1) + self.countWays(n-2)
        """