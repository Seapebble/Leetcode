class Solution:
    def isPalindrome(self, s: str) -> bool:
        preprocess = []
        for letter in range(len(s)):
            if s[letter].isalnum():
                preprocess.append(s[letter].lower())
        s=("".join(preprocess))
        front = 0
        back = len(s) -1
        while front < back:
            if(s[front] != s[back]):
                return False
            front += 1
            back -= 1
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("race a car")) 
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))  