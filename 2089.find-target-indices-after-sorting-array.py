#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
from typing import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        list=[]
        nums.sort()
        for i in range(len(nums)):
            if target in nums:
                if nums[i]==target:
                    list.append(i)
            else:
                break
        return list


# @lc code=end

