class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        right = 0
        left = 0
        chars = {}
        
        while (right < len(s)):
            chars[s[right]] = chars.get(s[right], 0) + 1

            while (chars[s[right]] > 1):
                chars[s[left]] = chars.get(s[left], 1) - 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        return res