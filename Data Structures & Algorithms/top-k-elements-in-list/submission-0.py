import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # questions to ask will there always be k greater elements what if we have lesser than k unique elements?
        # what kind of elements arein the array, int, string
        # what if there is a draw between more than 1 element which one should we return or is there alwasy a unique answer
        # brute force we maintain a counter and then sort by the value and take the first or last k elements, time complexity would be O(nlogn) for sorting, space complexity would be O(n) for the counter
        # to make it more efficient we can use a priority queue in the form of a min heap to help us to increase efficiency
        counts = Counter(nums)
        pq = []
        for key, val in counts.items():
            heapq.heappush(pq, (val, key))
            if len(pq)>k:
                heapq.heappop(pq)
        return [k for v, k in pq]

        