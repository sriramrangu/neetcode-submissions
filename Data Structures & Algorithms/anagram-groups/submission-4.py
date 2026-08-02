class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        
        for s in strs:
            cs = [0] * 26
            for c in s:
                cs[ord(c) - ord("a")]  += 1
            hm[tuple(cs)].append(s)      
        return list(hm.values())       