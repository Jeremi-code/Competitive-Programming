#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxLength = max(len(word1), len(word2))
        result = ''
        for i in range(maxLength):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return result
# @lc code=end

