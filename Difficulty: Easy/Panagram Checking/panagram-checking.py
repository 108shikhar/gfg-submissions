class Solution:
    def checkPangram(self,s):
        #code here
        a=s.lower()
        b=set()
        for i, j in enumerate(a):
            x=a[i]
            if ('a'<=x<='z'):
                b.add(x)
        if len(b)==26:
            return True
        else:
            return False
        
        """
        x=set()
        for i, j in enumerate(s):
            y=s[i]
            if ('A'<=y<='Z') or ('a'<=y<='z'):
                x.add(y)
        m=''.join(x)
        n=m.lower()
        l=set(n)
        if len(l)==26:
            return True
        else:
            return False
        """