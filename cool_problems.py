"""
Longest Substring Without Repeating Characters

Runtime Complexity: O(N)
Space Complexity: number of possible unique characters = O(1) ?

This is called 'Sliding Window' type of solution
"""
def lengthOfLongestSubstring(s: str) -> int:
    tracked_chars = {}
    max_length = left = 0
    for right, ch in enumerate(s):
        # if duplicate char found in window, move left
        # pointer to after first of duplicate
        if ch in tracked_chars and left <= tracked_chars[ch]:
            left = tracked_chars[ch] + 1
        # if no duplicate, update max_length and add char to dict
        else:
            max_length = max(max_length, right - left + 1)
        tracked_chars[ch] = right
    return max_length

print(lengthOfLongestSubstring('pwwkew'))