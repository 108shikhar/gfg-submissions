class Solution:
    def longCommSubstr(self, s1, s2):
        # code here
        m=len(s1)-1
        n=len(s2)-1
        dp=[[None for c in range(n+1)] for r in range(m+1)]
        
        def lcstr(m,n):
            
            if m<0 or n<0:
                return 0
                
            if dp[m][n]!=None:
                return dp[m][n]
            
            if s1[m]==s2[n]:
                dp[m][n] = 1 + lcstr(m-1,n-1)
                
            else:
                dp[m][n] = 0
                
            lcstr(m,n-1)
            lcstr(m-1,n)
                
            return dp[m][n]
            
        lcstr(m,n)
        
        val=[]
        
        for r in range(0,m+1,1):
            large=max(dp[r][0:n+1:1])
            val.append(large)
            
        ans = max(val)
        
        return ans