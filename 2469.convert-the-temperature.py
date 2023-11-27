#
# @lc app=leetcode id=2469 lang=python3
#
# [2469] Convert the Temperature
#

# @lc code=start
from typing import List
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = abs(celsius) + 273.15
        fahrenheit = abs(celsius) * 1.80 + 32.00
        result = [kelvin, fahrenheit]
        return result
# @lc code=end

