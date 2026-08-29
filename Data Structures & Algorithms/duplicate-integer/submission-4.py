class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n), O(n) reduce this to O(1) using bit manipulation
        visited = set()
        for n in nums:
            if n not in visited:
                visited.add(n)
            else:
                return True
        return False
        