class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force can be to get the product of all of the elements and iterate through each element and divide by it, but we would need to take into accoutn edge cases such as dividing by zero
        # but to not use the divide operation it mean we would have to multiply only
        # in this case we woudl ened to build a prefix sum but wiht a slight twist without itself
        # we would keep track of two varibale one multiplying form the forn tand one form the back 
        front, back = 1, 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] *= front
            front *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            res[j] *= back
            back *= nums[j]

        return res
        
        