"""
Reverse Words in a String - Two-pointer approach

Given a string s, reverse the order of characters 
in each word within a sentence while still preserving 
whitespace and initial word order.
"""
def reverseWords(s: str) -> str:
    left = 0
    right = 0
    while right < len(s):
        while right < len(s) and s[right] != ' ':
            right += 1
        # i love this line
        s = s[:left] + s[left:right][::-1] + s[right:]
        right += 1
        left = right
    return s

"""
Reverse Words in a String - Cheeky One-liner
"""
def fastReverseWords(s: str) -> str:
    return ' '.join(s.split()[::-1])[::-1]

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