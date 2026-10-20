class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()
        max_l = 0
        left = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_l = max(max_l, right - left + 1)

        return max_l