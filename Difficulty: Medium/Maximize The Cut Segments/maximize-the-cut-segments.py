class Solution:
    def maximizeCuts(self, n, x, y, z):
        # code here
        dp=[None]*(n+1)
        
        def solve(n,x,y,z,dp):
        
            if n==0:
                return 0
            if n<0:
                return -1
                
            if dp[n]!=None:
                return dp[n]
                
            one = solve(n-x,x,y,z,dp)
            two = solve(n-y,x,y,z,dp)
            thr = solve(n-z,x,y,z,dp)
        
            ans = max(one, two, thr)
        
            if ans == -1:
                dp[n]=-1
            else:
                dp[n]=ans+1

            return dp[n]
        
        solve(n,x,y,z,dp)
        if solve(n,x,y,z,dp)==-1:
            return 0
        else:
            return solve(n,x,y,z,dp)