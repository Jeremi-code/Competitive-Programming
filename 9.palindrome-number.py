#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
from typing import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPalindrome = False
        number = str(x)
        if (number == number[::-1]):
            isPalindrome = True
        return isPalindrome
        
        
        
# @lc code=end

