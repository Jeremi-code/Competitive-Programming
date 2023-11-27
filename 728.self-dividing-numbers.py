#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers = []
        for num in range(left,right+1):
            value = str(num)
            if '0' in value :
                continue 
            else :
                for i in range(0,len(value)):
                    if (num % int(value[i]) != 0) :
                        break
                    elif (i == len(value)-1):
                        numbers.append(num)
        return numbers


        
# @lc code=end

