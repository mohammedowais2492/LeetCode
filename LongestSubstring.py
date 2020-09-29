# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = [-1]*200
        length = 0
        n = len(s)
        start_index = 0
        for c in range(n):
            if indices[ord(s[c])] >= start_index:
                temp_len = c - start_index
                if temp_len > length:
                    length = temp_len
                start_index = indices[ord(s[c])] + 1
                indices[ord(s[c])] = c
            else:
                indices[ord(s[c])] = c
        if n - start_index > length:
            return n - start_index
        return length
