#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from functools import cmp_to_key
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i]=str(n)
        def compare(n,m):
            if n+m > m+n:
                return -1
            else :
                return 0
        nums=sorted(nums,key=cmp_to_key(compare))
        return str(int("".join(nums)))

        
# @lc code=end

