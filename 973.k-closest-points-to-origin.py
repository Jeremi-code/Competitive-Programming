#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import math


class Solution:
    from typing import List
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        list=[]
   
        arr=[]

        nums=0
        for i in range(len(points)):
                nums=points[i][0] ** 2 + points[i][1] **2
                list.append(nums)
        for i in range(k):
             
             x=min(list)          
             index=list.index(x)
             arr.append(points[index])
             list[index]=100000000
             
        return arr

             

# X=Solution()
# print(X.kClosest([[-173,399],[62,-213],[71,282],[-45,851],[710,982],[493,985],[-529,-946],[-83,78],[624,-785],[877,-351],[500,-376],[-601,-305],[-23,-79],[-82,906],[-143,500],[-249,-260],[10,706],[-904,-632],[-402,458],[303,-970],[93,-552],[-362,-743],[705,986],[900,-524],[-680,-204],[-726,890],[-138,742],[-76,714],[813,474],[443,23],[-422,117],[768,214],[863,562],[728,-204],[778,147],[-56,-751],[240,454],[-106,-701],[-897,-770],[572,433],[-658,97],[-301,-466],[902,-371],[-38,-662],[-872,191],[659,294],[852,965],[-37,665],[541,-920],[-537,704]],20))     

# @lc code=end

