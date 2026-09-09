class Solution:
    def lcs(self, s1, s2):
        # code here
        i=len(s1)-1
        j=len(s2)-1
        dp=[[None for c in range(len(s2))] for r in range(len(s1))]
        def lcs(i,j):
            if i<0 or j<0:
                return 0
                
            if dp[i][j]!=None:
                return dp[i][j]
                
            if s1[i]==s2[j]:
                dp[i][j] = 1 + lcs(i-1,j-1)
                
            if s1[i]!=s2[j]:
                dp[i][j] = max(lcs(i,j-1),lcs(i-1,j))
                
            return dp[i][j]
                
        return lcs(i,j) 