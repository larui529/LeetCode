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
