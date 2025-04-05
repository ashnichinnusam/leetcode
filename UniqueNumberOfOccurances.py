class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        count = Counter(arr)
        occurrences = list(count.values())
        return len(occurrences) == len(set(occurrences))
