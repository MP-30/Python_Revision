"""
Easy
1 
nums = [2,7,11,15]
target = 9
class Solution:
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    
                    return [i,j]
                    
myrej = Solution.twoSum(nums, target)
print(myrej)

#Palindrome Number
x = 122217
class Solution:
    def isPalindrome( x: int) -> bool:
        y = str(x)
        z = y[::-1]
        if y == z:
            print (True)
        else: print(False)
pn = Solution.isPalindrome(x)

# Roman to Integer
x = "MCMXCIV"
y = []
class Solution:
    def romanToInt(s):
        x=str(s)
        for char in x:
            if char == "I":
                (y.append(1))
            elif char == "V":
                (y.append(5))
            elif char == "X":
                (y.append(10))
            elif char == "L":
                (y.append(50))
            elif char == "C":
                (y.append(100))
            elif char == "D":
                (y.append(500))
            elif char == "M":
                (y.append(1000))
        
        for i in range(1,len(y)):
            if y[-(i+1)] < y [-i]:
                y[-(i+1)] = -y[-(i+1)]
            else: pass
        
        print(sum(y))
ans = Solution.romanToInt(x)

#Longest Common Prefix
strs = ["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(strs):
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1 , len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix    
                
sol = Solution.longestCommonPrefix(strs)
print(sol)
"""

# Valid Parentheses
s = "()[]{}{{}}"
mapping = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
stack = []
class Solution:
    def isValid(s):
        for char in s:
            if char in mapping:  
                stack.append(char)
            elif stack and char == mapping[stack[-1]]:  
                stack.pop()
            else: 
                return False

        return not stack  


res = Solution.isValid(s)
print(res)
