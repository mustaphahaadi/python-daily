"""Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""



def reverse_string(s):
    return s[::-1]
# or
#    return ''.join(reversed(s))


string = input("Enter a string: ")
print(reverse_string(string))