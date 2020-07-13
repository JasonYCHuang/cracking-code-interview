class Solution:
    def palindrome(self, word):
        target = word.lower()

        h = {}
        l = 0
        for w in target:
            if w is not ' ':
                l += 1
                if w in h:
                    h[w] += 1
                else:
                    h[w] = 1
        
        limit = l % 2
        for _, v in h.items():
            if v % 2 == 1:
                limit -= 1

        if limit == 0:
            return True
        return False






s = Solution()
print(s.palindrome('Tact coa') == True)
print(s.palindrome('t a') == False)
print(s.palindrome('') == True)
print(s.palindrome('b') == True)