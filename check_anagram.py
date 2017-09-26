from collections import Counter

def check_anagram(s, t):
    """This is a function to check if some anagram of t is a substring of s"""

    # firstly rule out obvious unmatching cases
    if t==None:
        return None
    
    if len(t) > len(s):
        return False    
    
    s = s.lower() # make all letters lowercase
    t = t.lower()
    
    n = 0   # set counter
    for i in range(len(s)-len(t)+1):  # scan the same length of t through s string
        slice = s[i:(i+len(t))]
        if Counter(slice) == Counter(t):  # compare the letter count for each alphabet by using Counter class
            n+=1
            break
        else:
            continue
    
    if n > 0:
        return True
    else:
        return False