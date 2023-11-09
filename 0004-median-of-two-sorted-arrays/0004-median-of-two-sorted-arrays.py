class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            n = len(nums1)
            m = len(nums2)

            if n > m:
                return self.findMedianSortedArrays(nums2, nums1)

            lo = 0
            hi = n 
            left = (n + m + 1) // 2

            while lo <= hi:
                mid = lo + (hi - lo) // 2
                i1 = mid
                i2 = left - i1 

                MaxA = float('-inf') 
                MinA = float('inf')  
                MaxB = float('-inf') 
                MinB = float('inf')  

                if (i1 - 1) > -1:
                    MaxA = nums1[i1 - 1]
                if i1 < n:
                    MinA = nums1[i1]
                if (i2 - 1) > -1:
                    MaxB = nums2[i2 - 1]
                if i2 < m:
                    MinB = nums2[i2]

                if MaxA <= MinB and MaxB <= MinA:
                    if (n + m) % 2 == 1:
                        return float(max(MaxA, MaxB))
                    else:
                        return (max(MaxA, MaxB) + min( MinA, MinB)) / 2.0
                elif MaxA > MinB:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return 0