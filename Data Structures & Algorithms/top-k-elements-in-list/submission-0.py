from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        common = counter.most_common(k)
        result = []
        for item in common:
            result.append(item[0])
        return result
