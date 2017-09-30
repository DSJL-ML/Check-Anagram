def check_anagram(s, t):
    """This is a function to check if some anagram of t is a substring of s using sorting method"""

    # firstly rule out obvious unmatching cases
    if t==None:
        return None

    if len(t) > len(s):
        return False   

    s = s.lower() # make all letters lowercase
    t = t.lower()

    sort_t = sorted(t) # merge sort t

    n = 0 # set counter
    for i in range(len(s)-len(t)+1): # scan the same length of t through s string
        slice = s[i:(i+len(t))]
        sort_slice = sorted(slice)   # merge sort string slice from s
        if sort_slice == sort_t:     # compare sorted strings
            return True
            n+=1
            break
	else:
            continue	

    if n > 0:
        return True
    else:
        return False