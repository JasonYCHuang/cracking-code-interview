class Solution:
    def oneAway(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        if abs(l1 - l2) > 1:
            return False
        w1, w2 = word1, word2
        if l1 > l2:
            w1, w2 = w2, w1

        i, j, opLimit = 0, 0, 1
        while i < l1 and j < l2 and opLimit >= 0:
            if w1[i] == w2[j]:
                i += 1
                j += 1
            else:
                if i + 1 < l1 and w1[i + 1] == w2[j]:
                    i += 2
                    j += 1
                    opLimit -= 1
                elif j + 1 < l2 and w1[i] == w2[j + 1]:
                    i += 1
                    j += 2
                    opLimit -= 1
                elif i + 1 < l1 and j + 1 < l2 and w1[i + 1] == w2[j + 1]:
                    i += 2
                    j += 2
                    opLimit -= 1
                else:
                    return False
        
        if opLimit >= 0:
            return True
        return False


s = Solution()
print(s.oneAway('pale', 'ple') == True)
print(s.oneAway('pales', 'pale') == True)
print(s.oneAway('pale', 'bale') == True)
print(s.oneAway('pale', 'bake') == False)