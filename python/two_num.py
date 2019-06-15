'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class solution:

    def two_num(self, nums, target):
        dict = {}
        for index, num in enumerate(nums):  # {(0, 2), (1, 7),(2, 11)}
            another_num = target - num
            if another_num in dict:
                return [dict[another_num], index]
            dict[num] = index
        return None


nums = [2, 3, 4, 7, 11, 15]
target = 9
print(solution().two_num(nums, target))
