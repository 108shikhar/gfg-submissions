class Solution:
    def findMinInsertions(self, s):
        # code here
        t=''.join(reversed(s))
        if t==s:
            return 0
        else:
            m=len(s)-1
            n=len(t)-1
            dp=[[None for c in range(n+1)] for r in range(m+1)]
            def ilps(m,n):
                if m<0 or n<0:
                    return 0
                if dp[m][n]!=None:
                    return dp[m][n]
                if s[m]==t[n]:
                    dp[m][n]=1+ilps(m-1,n-1)
                elif s[m]!=t[n]:
                    dp[m][n]=max(ilps(m-1,n),ilps(m,n-1))
                return dp[m][n]
            ilps(m,n)
            ans=len(s)-ilps(m,n)
            return ans