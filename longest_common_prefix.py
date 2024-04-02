class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current = -1
        min_length = len(min(strs,key=len))
        prefix_common = "" 
        for i in range(min_length) :
            letters = [words[i] for words in strs] 
            if all(letter == letters[0] for letter in letters) :
                prefix_common += letters[0]
            else :break
        return prefix_common




        