class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)

        # abbba

        for i in range(len(s)):
            l = i - 1 # 0
            r = i + 1 # 2
            curr = i
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    res += 1
                else:
                    break
                l -= 1
                r += 1

            r = i + 1
            while r <= len(s) - 1 and curr >= 0:
                if s[curr] == s[r]:
                    res += 1
                else:
                    break
                r += 1
                curr -= 1
        
        return res
        





        
        