class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketMap = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        bracketStack = []
        for bracket in s:
            if bracket not in bracketMap:
                bracketStack.append(bracket)
            else:
                if bracketStack and bracketMap[bracket] == bracketStack[-1]:
                    bracketStack.pop()
                else:
                    return False

        if bracketStack:
            return False

        return True
