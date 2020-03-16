from typing import List
import collections

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        N, M = len(grid), len(grid[0])

        found_servers = [] # store all found servers
        count_connected_servers = 0 # count how many found servers have at least one connection

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    found_servers.append((i,j))

        for server1 in found_servers:
            for server2 in found_servers:
                if server1 is not server2:
                    if server1[0] == server2[0] or server1[1] == server2[1]:
                        count_connected_servers += 1
                        break

        return count_connected_servers
        """Analysis
        - time: O(n*m)
        - space: O(n+m)
        """


class Solution2():
    # super consise solution by user macheret
    # from https://leetcode.com/problems/count-servers-that-communicate/discuss/538387/Python-3-1-line-faster-than-100
    def countServers(self, grid: List[List[int]]) -> int:
        computers = [(x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell]
        cols, rows = map(collections.Counter, zip(*computers))
        return sum(rows[y] > 1 or cols[x] > 1 for x, y in computers)

### TEST CODE ###

s = Solution()

test_cases = [
    (0, [[1,0],[0,1]]),
    (3, [[1,0],[1,1]]),
    (4, [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]),
    (3, [[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]),
]

count_passes = 0

for expected_output, test in test_cases:
    print("="*50)
    print(f"INPUT: {test}")

    output = s.countServers(test)

    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}\n")
    
    if output == expected_output:
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")

print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.\n")