class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for c in w:
                index = ord(c) - ord('a')
                count[index]+=1
            key = tuple(count)
            groups[key].append(w)
        return list(groups.values())
        
        