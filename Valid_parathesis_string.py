
# https://leetcode.com/problems/valid-parenthesis-string/
class Solution:
    def checkValidString(self, s: str) -> bool:
        while s != s.replace("()", ""):
            s = s.replace("()", "")
        if s == "" : return True
        queue = [] 
        for i in range(len(s)) : 
            if s[i] in ["*", "("] : 
                queue.append(1)
            else :
                if queue  : 
                    queue.pop() 
                else : 
                    return False
        queue = [] 
        s = s[::-1]
        for i in range(len(s)) : 
            if s[i] in ["*", ")"] : 
                queue.append(1)
            else :
                if queue  : 
                    queue.pop() 
                else : 
                    return False
        return True
        