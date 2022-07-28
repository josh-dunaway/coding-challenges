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