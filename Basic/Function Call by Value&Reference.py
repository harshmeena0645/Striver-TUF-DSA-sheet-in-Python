class Solution:
    def passedBy(self, a, b):
        a += 1
        b += 2
        return a, b

sol = Solution()
a = 10
b = 20
result = sol.passedBy(a, b)
print(result)
