import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # questions to ask will there always be k greater elements what if we have lesser than k unique elements?
        # what kind of elements arein the array, int, string
        # what if there is a draw between more than 1 element which one should we return or is there alwasy a unique answer
        # brute force we maintain a counter and then sort by the value and take the first or last k elements, time complexity would be O(N+UlogU) n for counter and k how many hash keys we have space xomplexity owuld be O(k)
        # to make it more efficient we can use a priority queue in the form of a min heap to help us to increase efficiency
        counts = Counter(nums)
        """
        pq = []
        for key, val in counts.items():
            heapq.heappush(pq, (val, key))
            if len(pq)>k:
                heapq.heappop(pq)
        return [k for v, k in pq]
        """
        # time complexity is O(n+Ulogk) for the counter, space complexity O(n)
        # to make it even more efficient we can use bucket sort
        # like that we can sort them accoridn got frequency since we do not need to return them in order
        # to make it even more efficient we cna use bucket sort which leads to a 
        bucket = [[] for _ in range(len(nums)+1)]
        for nums, freq in counts.items():
            bucket[freq].append(nums)
        res = []
        for freq in range(len(bucket)-1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
            if len(res)==k:
                return res

        

        