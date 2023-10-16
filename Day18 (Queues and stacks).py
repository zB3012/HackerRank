import sys

class Solution:
    # Code here
    stack=[]
    queue=[]

    def __init(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.insert(0,ch)
    
    def enqueueCharacter(self, ch):
        self.queue.append(ch)
    
    def popCharacter(self):
        return self.stack.pop(0)
    
    def dequeueCharacter(self):
        return self.queue.pop(0)

s=input()
#Create solution class object
obj=Solution()

l=len(s)
# Push all characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''pop the top character from stack
dequeue the first character from queue
compare both the charactres
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break

if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")