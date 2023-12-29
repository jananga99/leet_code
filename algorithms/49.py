from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash=defaultdict(list)
        for s in strs:
            w=''.join(sorted(s))
            hash[w].append(s)
        return hash.values()