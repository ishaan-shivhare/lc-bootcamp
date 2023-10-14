class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_map = collections.defaultdict(list)
        t_map = collections.defaultdict(list)

        for i in range(len(s)):
            s_map[s[i]].append(i)
            t_map[t[i]].append(i)


        if list(s_map.values()) == list(t_map.values()):
            return True
        return False
