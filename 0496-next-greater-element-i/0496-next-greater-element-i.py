class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = {}
        stack = []
        ans = []
        
        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[stack[-1]] <= nums2[i]:
                stack.pop()
            
            if stack:
                cache[nums2[i]] = nums2[stack[-1]]
            else:
                cache[nums2[i]] = -1
            
            stack.append(i)
            
        for i in nums1:
            ans.append(cache[i])
        
        return ans