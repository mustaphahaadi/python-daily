"""
Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
"""

def palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return True if len(s) <= 1 else (s[0] == s[-1]) and palindrome(s[1:-1]) 


# Simple solution using slicing
def palindrome_simple(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]