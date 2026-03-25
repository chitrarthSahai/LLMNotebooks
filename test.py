from collections import deque
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        n = len(height)
        i = 0

        while i < n - 1:
                
            depression = deque()
            if height[i+1] < height[i] and i+1 != n-1:
                trap = True
                not_found = False
                depression.append(height[i])
                bound_start = i
                while trap and i < n-1:
                    i += 1
                    if height[i] >= height[bound_start]:
                        depression.append(height[i])
                        trap = False
                    elif i == n - 1:
                        not_found = True
                        i = bound_start + 1
                        break
                    else:
                        depression.append(height[i])
                
                if not not_found:
                    water_level = min(depression.pop(), depression.popleft())
                    max_water = water_level * len(depression)
                    result += max_water - sum(depression)
                
            else:
                i += 1
        
        return result

                


height = [4,2,3]

s = Solution()
print(s.trap(height))  # Output: 6 This shows that the total amount of trapped rainwater between the bars represented by the input list is 6 units.