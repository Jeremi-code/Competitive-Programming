class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict = {}
        for i in range(len(sentence)) :
            if sentence[i] in dict :
                dict[sentence[i]] += 1
            else :
                dict[sentence[i]] = 1
        dict_keys = list(dict.keys())
        if len(dict_keys) >=26 :
            return True
        else :
            return False