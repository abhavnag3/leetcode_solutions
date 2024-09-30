class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hmap = {}
        for i in range(len(s)):
            if s[i] in hmap.keys():
                hmap[s[i]] = [hmap[s[i]][0] + 1, i]
            else:
                hmap[s[i]] = [1, i]
        
        print(hmap)
        
        for key in hmap.keys():
            if hmap[key][0] == 1:
                return hmap[key][1]
        return -1
        