"""
给定整数数组 nums 和目标值 target，找出和为 target 的两个整数的数组下标，并返回它们。
每种输入只对应一个答案，不能使用相同元素两次。返回顺序不限。
示例:
输入: nums = [2,7,11,15], target = 9 输出: [0,1]
输入: nums = [3,2,4], target = 6 输出: [1,2]
输入: nums = [3,3], target = 6 输出: [0,1]
提示:
- 只有一个有效答案
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        for i, num in enumerate(nums):
            if target - num in complementMap:
                return [complementMap[target - num], i]
            complementMap[num] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
