def lengthOfLongestSubstring(s: str) -> int:
    if not s: return 0
    start, end = 0, 1
    seen = set()
    seen.add(s[0])
    res = 1
    
    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            length = end - start + 1
            res = max(res, length)
        
        else:
            while s[start] != s[end]:
                seen.remove(s[start])
                start += 1
            start += 1
        end += 1
    
    return res


# Runtime: 62 ms, faster than 89.39% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 95.59% of Python3 online submissions for Longest Substring Without Repeating Characters.