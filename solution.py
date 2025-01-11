class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        length, result = len(digits) - 1, 0
        for digit in digits:
            result += 10**length * digit
            length -= 1
        return [int(digit) for digit in str(result + 1)]


if __name__ == "__main__":
    solution = Solution()
    print(f"Input: [1,2,3]\nOutput: {solution.plusOne([1,2,3])}")
