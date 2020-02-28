class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        water = 0
        latest_end = 0

        for i, h1 in enumerate(height):
            if(i < latest_end):
                print(f"skipping i: {i}")
                continue
            print(f"computing i: {i}")
            if h1 > 0:
                largest_so_far, largest_so_far_index = 0, -1 # in case there's no j s.t. height[j] >= height[i]
                for j, h2 in enumerate(height[i+1:-1]):
                    if h2 >= largest_so_far:
                        largest_so_far = h2
                        largest_so_far_index = j
                    if h2 >= h1:
                        print(f"============ height[{i+j+1}]:{h2} >= height[{i}]:{h1} ============")
                        volume = self.sum_volume(height, i, h1, i+j+1, h2)
                        print(f"volume: {volume}") # sum volume between h1 and h2
                        water += volume
                        latest_end = i+j+1
                        break

        return water

    def sum_volume(self, height, i, h1, j, h2):
        smaller = min(h1, h2)
        volume = 0

        # TODO: check if there's a trough for water to collect
        #       i.e. height must first decrease then increase
        #       AND height cannot be strictly descrings or increasing

        for idx in range(i+1, j):
            volume += smaller - height[idx]

        return volume

      
### TEST CODE ###

s = Solution()

test_cases = [
    (6, [0,1,0,2,1,0,1,3,2,1,2,1]),
    (94, [9,0,1,0,2,1,0,1,3,2,1,2,1,9]),
    (0, [9,8,7,6,5]),
    (0, [5,6,7,8,9]),
    (0, [1,1,1,1,1]),
    (0, [0]),
    (0, [0,0])
]

count_passes = 0

for expected_output, test in test_cases:
    print("="*50)
    print(f"INPUT: {test}")

    output = s.trap(test)

    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}\n")
    
    if output == expected_output:
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")

print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.\n")
