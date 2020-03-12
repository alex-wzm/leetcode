from typing import List

class Solution:
    def convertToBase7(self, num: int) -> str:
        output = ''
        is_negative = False

        if num < 0:
            num = -num
            is_negative = True


        while num > 0:
            output = str(num % 7)+output
            num = num // 7

        return "-"+output if is_negative else output


### TEST CODE ###

s = Solution()

test_cases = [
    ("202", 100),
    ("-10", -7),
]

count_passes = 0

for expected_output, input in test_cases:
    print("="*50)
    print(f"INPUT: ({input})")

    output = s.convertToBase7(input)

    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}\n")
    
    if output == expected_output: # TODO
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")

print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.\n")
