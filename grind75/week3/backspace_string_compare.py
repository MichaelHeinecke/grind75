class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_res = []
        for c in s:
            if c == "#":
                if len(s_res) > 0:
                    s_res.pop()
            else:
                s_res.append(c)

        t_res = []
        for c in t:
            if c == "#":
                if len(t_res) > 0:
                    t_res.pop()
            else:
                t_res.append(c)

        return s_res == t_res
