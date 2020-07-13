import collections

# class Solution:
#     def isUnique(self, word):
#         h = collections.defaultdict(bool)

#         for w in word:
#             if w in h:
#                 return False
#             h[w] = True

#         return True

class Solution:
    def isUnique(self, word):
        h = {}

        for w in word:
            if w in h:
                return False
            h[w] = True

        return True

s = Solution()
print(s.isUnique('abc') == True)

print(s.isUnique('aabc') == False)

print(s.isUnique('abcc') == False)