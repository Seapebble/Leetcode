from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for num in nums:
            if num % 2 == 0: even.append(num)
            else: odd.append(num)
        even.sort()
        odd.sort()
        return [*even, *odd]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParity([3, 1, 2, 4])) 
    print(solution.sortArrayByParity([0]))  