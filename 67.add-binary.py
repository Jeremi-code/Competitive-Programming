#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a:str, b: str) -> str:
        sum=bin(int(a,2) + int(b,2))
        return sum[2:]

        
# @lc code=end

