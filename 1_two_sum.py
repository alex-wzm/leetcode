from typing import List
        
class Solution1: # Time Limit Exceeded
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i != j:
                    if n1 + n2 == target:
                        return [i, j]
                        """
                        Analysis:
                        - Time: O(n^2)
                        - Space: O(1)
                        """
 


### TEST CODE ###

s = Solution1()

test_cases = [
    ([0,1], ([1,1,2], 2)),
    ([0,1], ([1,1,2], 2)),
    ([0,1], ([2,7,11,15], 9)),
    ([1,2], ([3,2,4], 6)),
]

count_passes = 0

for expected_output, test in test_cases:
    print("="*50)
    print(f"INPUT: {test}")

    output = s.twoSum(test[0], test[1])

    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}\n")
    
    if output == expected_output:
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")

print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.\n")
