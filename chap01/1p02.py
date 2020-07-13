class Solution:
    def samePermutation(self, word1, word2):
        if len(word1) != len(word2):
            return False

        h = {}
        for w in word1:
            if w in h:
                h[w] += 1
            else:
                h[w] = 1
        for w in word2:
            if w in h:
                c = h[w] - 1
                if c < 0:
                    return False
                h[w] = c
            else:
                return False
        
        for _, v in h.items():
            if v > 0:
                return False

        return True

s = Solution()
print(s.samePermutation('abc', 'cba') == True)
print(s.samePermutation('a', 'a') == True)
print(s.samePermutation('aaa', 'aaa') == True)
print(s.samePermutation('ab', 'ba') == True)
print(s.samePermutation('', '') == True)
print(s.samePermutation('abc', 'cbba') == False)
print(s.samePermutation('123', 'cbba') == False)
print(s.samePermutation('aaa', 'aaaa') == False)
print(s.samePermutation('abc', 'dac') == False)