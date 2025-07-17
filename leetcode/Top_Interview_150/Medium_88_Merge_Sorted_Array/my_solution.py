class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = index2 = 0

        nums1_copy = nums1[:]
        nums2_copy = nums2[:]
        
        result_index = 0
        
        while index1 < m and index2 < n:
            num1 = nums1_copy[index1]
            num2 = nums2_copy[index2]

            min_num = 0

            if (num1 < num2):
                min_num = num1
                index1 += 1
            else:
                min_num = num2
                index2 += 1

            nums1[result_index] = min_num

            result_index += 1
        
        while (index1 < m):
            remain_num = nums1_copy[index1]
            index1 += 1

            nums1[result_index] = remain_num
            result_index += 1

        while (index2 < n):
            remain_num = nums2_copy[index2]
            index2 += 1

            nums1[result_index] = remain_num
            result_index += 1


                

            

        