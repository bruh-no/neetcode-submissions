class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            hashMap[key].append(word)
        
        return list(hashMap.values())
