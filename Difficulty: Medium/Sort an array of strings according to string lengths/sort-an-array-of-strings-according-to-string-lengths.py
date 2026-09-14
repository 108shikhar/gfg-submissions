class Solution:
    def sortByLength(self, arr):
        # code here
        """
        m=len(arr)
        for i in range(1,m,1):
            x=len(arr[i])
            y=arr[i]
            j=i-1
            while j>=0 and x<len(arr[j]):
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=y
            """
        if len(arr) <= 1:
            return arr

        m = len(arr) // 2

        a = self.sortByLength(arr[:m])
        b = self.sortByLength(arr[m:])

        c = []

        i = 0
        j = 0

        while i < len(a) and j < len(b):

            if len(a[i]) <= len(b[j]):
                c.append(a[i])
                i = i + 1

            else:
                c.append(b[j])
                j = j + 1

        while i < len(a):
            c.append(a[i])
            i = i + 1

        while j < len(b):
            c.append(b[j])
            j = j + 1

        arr[:] = c
        return arr