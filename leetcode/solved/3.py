class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = dict()
        
        start, end = 0, 0
        result = 0

        while end < len(s):
            try:
                while check[s[end]]:
                    check[s[start]] = False
                    start += 1
            except:
                pass
            finally:
                check[s[end]] = True

            end += 1
            result = max(result, end - start)

        return result