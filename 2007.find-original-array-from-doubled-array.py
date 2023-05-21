#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#

# @lc code=start
import collections
from typing import List
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        cnts = collections.Counter(changed)
        for x in sorted(cnts.keys()):
            if cnts[x] > cnts[2*x]:
                return []
            cnts[2*x] -= cnts[x] if x else cnts[x]//2
        return list(cnts.elements())

print(Solution().findOriginalArray([1,3,4,2,6,8]))
 # @lc code=end

