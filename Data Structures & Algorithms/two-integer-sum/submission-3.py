class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1

            if num2 in visited:
                return [visited[num2], i]
            
            visited[num1] = i
            
        return []
        
                        