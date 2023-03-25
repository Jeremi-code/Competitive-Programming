#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()[::-1]
        length=0
        i=0
        if " " not in s:
            length=len(s)
        else:
            while i<len(s):
                if s[i]==" ":
                    break
                else:
                    length+=1
                    i+=1

        return length

        
# @lc code=end

