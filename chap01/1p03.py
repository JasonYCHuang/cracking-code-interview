class Solution:
    def urlify(self, url):
        l = len(url)
        if l == 0:
            return url

        target = url
        for i in range(l):
            if target[i]:
                next
            else:
                j = i + 1
                while not target[j] and j < l:
                    j += 1
                if j == l:
                    return target[:i]
                
                pass
            # for j in range(i + 1, l):
                



s = Solution()
print(s.urlify('Mr John   Smith     ') == 'Mr%20John%20Smith')