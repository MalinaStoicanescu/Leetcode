class Solution(object):
    def majorityElement(self, nums):
        
        length = len(nums)/2
        if len(nums) == 1:
            return nums[0]
        hash_map = {}
        for num in nums:
            if num in hash_map.keys():
                hash_map[num] += 1
                if hash_map[num] > length:
                    return num
            else:
                hash_map[num] = 1