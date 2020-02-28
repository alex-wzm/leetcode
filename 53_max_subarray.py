from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # init output to min_value and
        # init accumulator "current_max"
        max_so_far = float('-inf')
        current_max = 0
        
        for i in range(0, len(nums)):
            # accumulate current_max
            current_max = current_max + nums[i]

            # store if max sum so far
            if max_so_far < current_max:
                max_so_far = current_max
            
            # reset accumulator if value < 0
            # i.e. restart counting with next sub-array
            if current_max < 0:
                current_max = 0
                
        return max_so_far
        """
        Analysis:
            - O(n) time
            - O(n) space
        """
        

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

#         # base case
#         if len(nums) == 1:
#             return nums[0]
        
#         # init output to min_value
#         max_so_far = float('-inf')
        
#         # compare all sub arrays by recursively by storing max of
#         # - max_so_far
#         # - sum of nums (current sub array)
#         # - and sum of nums[i:-1] (pop current sub array)
#         for i in range(0, len(nums)):
#             max_so_far = max(
#                 max_so_far,
#                 sum(nums),
#                 self.maxSubArray(nums[i:-1])
#             )
            
#         return max_so_far

### TEST CODE ###

s = Solution()

test_cases = {
    # expected_output: case
    6: [-2,1,-3,4,-1,2,1,-5,4],
    1: [-2, 1],
}

count_passes = 0

for expected_output, test in test_cases.items():
    print("="*50)
    print(f"INPUT: {test}")
    output = s.maxSubArray(test)
    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}")
    print()
    if output == expected_output:
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")

print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.")