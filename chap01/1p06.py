class Solution:
    def compress(self, word):
        l = len(word)
        if l <= 1:
            return word

        target = ''
        i, j = 0, 1
        while i < l and j <= l:
            if (j == l) or (word[i] is not word[j]):
                target = target + word[i] + str(j - i)
                i = j
            j += 1
        if len(target) > l:
            return word
        return target


s = Solution()
print(s.compress('aabcccccaaa') == 'a2b1c5a3')
print(s.compress('abc') == 'abc')
print(s.compress('a') == 'a')
print(s.compress('') == '')