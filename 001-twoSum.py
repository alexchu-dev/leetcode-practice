from typing import List
class Solution:
    def twoSum(self, nums: List[int]=[], target: int=0) -> List[int]:
        """Find out the indices of two integers, if the target can be produced by adding up any of two num from the list.
        Parameters: A list of integers, target integer
        Returns: The indices of the two numbers which can produce the target
        Exception: In the case if the target cannot be produced, return blank list.
        """
        num_map = {}    # Initiate a blank dictionary, which will work as a map to hold the numbers
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i
        return []

y = Solution()
print(y.twoSum([1,3,5,7],8))