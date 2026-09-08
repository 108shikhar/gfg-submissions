class Solution:
    def minCost(self, height: list[int]) -> int:
        # code here
        i=0
        dp=[None]*(len(height)+1)
        def solve(i):
            if i>=len(height)-1:
                return 0
                
            if dp[i]!=None:
                return dp[i]
                
            if i+1<len(height):
                ans = abs(height[i+1]-height[i]) + solve(i+1)
                
            if i+2<len(height):
                two = abs(height[i+2]-height[i]) + solve(i+2)
                
                ans=min(ans,two)
                
            dp[i]=ans
            return dp[i]
         
        return solve(i)