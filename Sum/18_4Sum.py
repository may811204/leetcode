class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # O(n^3), O(1)
        if len(nums) < 4: return []
        nums.sort()
        res = []
        
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                
                l, r = j + 1, len(nums)-1
                while l < r:
                    s = nums[l] + nums[r] + nums[i] + nums[j]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[l], nums[r], nums[i], nums[j]])
                        while l < r and nums[l] == nums[l+1]: l += 1
                        while l < r and nums[r] == nums[r-1]: r -= 1
                        l += 1; r -= 1
        return res