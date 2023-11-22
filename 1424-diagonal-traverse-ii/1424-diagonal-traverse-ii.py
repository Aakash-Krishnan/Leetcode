class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        size, index, MaxSum = 0, 0, 0
        Map = [[] for _ in range(100001)]
        
        for i in range(len(nums)):
            size += len(nums[i])
            for j in range(len(nums[i])):
                Sum = i + j
                Map[Sum].append(nums[i][j])
                MaxSum = max(MaxSum, Sum)
        
        result = [0] * size
        
        for i in range(MaxSum + 1):
            current = Map[i]
            for j in range(len(current)-1, -1, -1):
                result[index] = current[j]
                index += 1
        return result