#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        sentence=""
        list=s.split()
        for i in range(1,len(list)+1):
            for j in range(len(list)):
                if str(i) in list[j]:
                    list[j]=list[j].removesuffix(str(i))
                    sentence+=list[j]+ " "
                    break


        return sentence.strip()



        
# @lc code=end

