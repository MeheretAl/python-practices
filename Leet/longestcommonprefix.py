def longestCommonPrefix(strs:list[str]) -> str:
        res = ""
        prefix = strs[0]
        for s in strs:
            prefix = prefix if len(prefix) < len(s) else s
        for i in range(len(prefix)):
            for s in strs:
                if i == len(s) or s[i] != prefix[i]:
                    return res
            res += strs[0][i]
        return res