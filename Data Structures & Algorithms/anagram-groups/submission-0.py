from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force method sort eahc string by their char and add them into a hashmap 
        # time complexity would be O(n * klogk) n would be the number of strings and k would be the length of the longest string
        # space complexity would be O(k*n) mainly for storing the hash keys
        # more efficient is to not sort
        visited = defaultdict(list)
        for string in strs:
            counts = [0]*26
            for char in string:
                counts[ord(char)-ord("a")]+=1
            visited[tuple(counts)].append(string)
        return list(visited.values())
        # for this solution more efficient time complexity of O(n*k) becasue for each word we are checking through words of len(h)
        # space complexity would be O(n) because each hash key is a set length
        