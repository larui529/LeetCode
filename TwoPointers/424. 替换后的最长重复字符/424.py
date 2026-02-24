def characterReplacement(s: str, k: int) -> int:
    count = [0] * 26
    left = 0
    max_count = 0
    ans = 0
    for right, ch in enumerate(s):
        idx = ord(ch) - ord('A')
        count[idx] += 1
        max_count = max(max_count, count[idx])
        while (right - left + 1) - max_count > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans


if __name__ == '__main__':
    print(characterReplacement("AABABBA", 1))

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0 # [l, r]
        freq = defaultdict(int)
        max_count = 0
        res = 0

        for i in range(n):
            r = i
            freq[s[r]] += 1
            max_count = max(max_count, freq[s[r]])
            replace_n = r - l +1 - max_count
            while replace_n >k:
                freq[s[l]] -= 1
                l += 1
                max_count = max(max_count, freq[s[r]])
                replace_n = r - l +1 - max_count
            res = max(res, r-l+1)
        return res

