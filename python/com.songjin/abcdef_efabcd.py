"""
三次逆转
切片拼接
列表拼接
"""


class Solution:

    def __init__(self):
        self.abcdef = "abcdef"
        self.nums = "12345"
        self.language = "python"
        self.index = 4

    def reverse_words(self, s: str, index: int):
        # [0:index:1] 从0到n步长为1
        # [-1::-1] 第一个参数起:到末尾:步长-1为反向
        s1 = s[0:index:1][-1::-1]  # dcba
        s2 = s[index::1][-1::-1]  # fe
        return (s1 + s2)[-1::-1]

    def reverse_words2(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

    def reverse_words3(self, s: str, n: int) -> str:
        result = []
        for i in range(n, len(s)):
            result.append(s[i])
        for i in range(n):
            result.append(s[i])
        return ''.join(result)


s = Solution()

result = s.reverse_words(s.nums, s.index)
print(result)

result = s.reverse_words2(s.abcdef, s.index)
print(result)

result = s.reverse_words3(s.language, s.index)
print(result)
