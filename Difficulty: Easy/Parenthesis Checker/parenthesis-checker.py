class Solution:
    def isBalanced(self, s):
        # code here
        def string(s):
            stk=[]
            for i in s:
                if i in ('(','{','['):
                    stk.append(i)
                else:
                    if not stk:
                        return False
                    elif match(stk[-1],i)==False:
                        return False
                    elif match(stk[-1],i)==True:
                        stk.pop()
            if not stk:
                return True
            else:
                return False
        def match(a,b):
            if a=='(' and b==')':
                return True
            if a=='[' and b==']':
                return True
            if a=='{' and b=='}':
                return True
            else:
                return False
        return string(s)