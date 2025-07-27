class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = (len(nums) - k) % len(nums)
        arr1 = nums[:i]
        arr2 = nums[i:]

        print(f'arr1: {arr1}')
        print(f'arr2: {arr2}')
        nums[:] = arr2 + arr1
        print(nums)
        
        