from collections import Counter


def findAnagrams(s: str, p: str) -> list[int]:
    def _is_anagram(one: str, two: str):
        return Counter(one) == Counter(two)

    l, r = 0, len(p) - 1

    res = []
    while r < len(s):
        if _is_anagram(p, s[l : r + 1]):
            res.append(l)
        l += 1
        r += 1
    return res


if __name__ == "__main__":
    s, p = "cbaebabacd", "abc"
    result = findAnagrams(s, p)
    print(result)
