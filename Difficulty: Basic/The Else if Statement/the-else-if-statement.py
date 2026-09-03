class Solution:
    def utility(self, number):
        # code here
        if number>100:
            print("Big")
        elif number<=100 and number>10:
            print("Number")
        else:
            print("Small")