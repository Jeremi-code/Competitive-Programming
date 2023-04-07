#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list=[]
        count=0
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[i]>nums[j]:
                    count+=1
                
            list.append(count)
        return list
# @lc code=end

