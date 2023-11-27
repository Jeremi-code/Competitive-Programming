#
# @lc app=leetcode id=2413 lang=python3
#
# [2413] Smallest Even Multiple
#

# @lc code=start
from typing import List
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n > 150:
            return 0
        if n % 2 == 0:
            return n
        return n * 2
# @lc code=end

