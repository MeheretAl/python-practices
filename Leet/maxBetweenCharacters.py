def maxLengthBetweenEqualCharacters(s: str) -> int:
    dict1 = {}
    dict2 = {}
    for i in range(len(s)):
        if s[i] in dict1:
            dict2[s[i]] = i - dict1[s[i]] - 1
        else:
            dict1[s[i]] = i
    curr = 0
    for keys, values in dict2.items():
        curr = max(values, curr)

    return curr if dict2 else -1


'''
    There exists another approach using less lines of code but this is concise and
    easy to understand so will leave it as is but will try to decrease the maps 
    to just one
'''
