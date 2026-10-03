class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
sol = Solution()
n = 5
result = sol.countBits(n)
print(f"n = {n}")
print(f"Output: {result}")