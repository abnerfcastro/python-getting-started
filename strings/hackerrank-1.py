import sys

def super_reduced_string(s):
    i = 0
    while True:
        if ((i+2) <= len(s)):
            if (s[i] == s[(i+1)]):
                s = s[:i] + s[(i+2):]
                i = (i - 1) if (i > 0) else 0
            else:
                i += 1
        else:
            break
    # Return value
    if (s == ""):
        return "Empty String"
    else:
        return s

s = input().strip()
result = super_reduced_string(s)
print(result)