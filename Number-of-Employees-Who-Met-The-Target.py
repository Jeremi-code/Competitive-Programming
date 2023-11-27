from typing import List
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        isGreaterThanTarget = list(map(lambda x : x>=target,hours))
        count = sum(isGreaterThanTarget)
        return count
