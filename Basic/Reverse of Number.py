class Solution(object):
    def reverse(self, x):
        temp=abs(x)
        num=0
        while temp!=0:
            m=temp%10
            num=num*10+m
            temp//=10
        
        if x<0:
            num=-num
            
        if num < -2**31 or num > 2**31 - 1:
            return 0

        return num