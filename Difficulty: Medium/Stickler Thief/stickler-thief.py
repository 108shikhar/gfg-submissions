class Solution:  
    def findMaxSum(self, arr):
        # code here
        dp=[None]*len(arr)
        i=0
        def solve(i):
            if i>=len(arr):
                return 0
            if dp[i]!=None:
                return dp[i]
            rob = arr[i] + solve(i+2)
            skip = solve(i+1)
            dp[i] = max(rob, skip)
            return dp[i]
        return solve(0)
        
        """
        Recursive Solution
        i=0
        def solve(i):
            if i>=len(arr):
                return 0
            rob = arr[i] + solve(i+2)
            skip = solve(i+1)
            return max(rob, skip)
        return solve(0)
        """