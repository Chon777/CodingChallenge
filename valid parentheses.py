class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket = list(s)
        dict = {"]":"[", "}":"{", ")":"("}
        
        for i in bracket:
            if i in dict.values():
                stack.append(i)
            elif i in dict.keys():
                if  stack == [] or stack.pop() != dict[i] :
                    return False
            else: 
                return False
        
        return  stack == []