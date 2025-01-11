class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for a in columnTitle:
            value = ord(a) - 64
            result = result * 26 + value
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.titleToNumber("AAC")) 
    print(solution.titleToNumber("A"))  