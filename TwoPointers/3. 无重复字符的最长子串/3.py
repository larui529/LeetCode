def lengthOfLongestSubstring(s: str) -> int:
    last = {}
    left = 0
    ans = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = i
        ans = max(ans, i - left + 1)
    return ans


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))
