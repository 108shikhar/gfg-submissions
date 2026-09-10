class Solution:
	def minOperations(self, s1, s2):
		# code here
		  m=len(s1)-1
          n=len(s2)-1
          dp=[[None for c in range(n+1)] for r in range(m+1)]
          def dots(m,n):
              if m<0 or n<0:
                  return 0
              if dp[m][n]!=None:
                  return dp[m][n]
              if s1[m]==s2[n]:
                  dp[m][n]=1+dots(m-1,n-1)
              elif s1[m]!=s2[n]:
                  dp[m][n]=max(dots(m-1,n),dots(m,n-1))
              return dp[m][n]
          val=dots(m,n)
          del1=len(s1)-val
          del2=len(s2)-val
          ans=del1+del2
          return ans