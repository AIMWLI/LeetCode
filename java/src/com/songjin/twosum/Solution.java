package com.songjin.twosum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 给定整数数组 nums 和目标值 target，找出和为 target 的两个整数的数组下标，并返回它们。
 * 每种输入只对应一个答案，不能使用相同元素两次。返回顺序不限。
 * 示例:
 * 输入: nums = [2,7,11,15], target = 9 输出: [0,1]
 * 输入: nums = [3,2,4], target = 6 输出: [1,2]
 * 输入: nums = [3,3], target = 6 输出: [0,1]
 * 提示:
 * - 只有一个有效答案
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> complementMap = new HashMap<>(nums.length);
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (complementMap.containsKey(complement)) {
                return new int[]{complementMap.get(complement), i};
            }
            complementMap.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        int[] result = new Solution().twoSum(new int[]{2, 7, 11, 15}, 9);
        System.out.println(Arrays.toString(result));
    }
}
