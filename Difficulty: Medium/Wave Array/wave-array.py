class Solution:
    def sortInWave(self, arr):
        # code here
        m=len(arr)
        for i in range(0,m,2):
            arr[i:i+2]=arr[i:i+2][::-1]
            