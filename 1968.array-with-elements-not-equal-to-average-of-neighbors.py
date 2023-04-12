#
# @lc app=leetcode id=1968 lang=python3
#
# [1968] Array With Elements Not Equal to Average of Neighbors
#

# @lc code=start

from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        l,r=0,len(nums)-1
        while l<=r:
            arr.append(nums[l])
            l+=1
            if l<r:
                arr.append(nums[r])
                r-=1

        return arr
    
# @lc code=end

