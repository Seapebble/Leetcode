pick = 6


class Solution:
    def guessNumber(self, n: int) -> int:
        lower, higher = 1, n
        while lower <= higher:
            nextGuess, responce = (mid := (lower + higher) // 2), guess(mid)
            if responce == 0:
                return nextGuess
            elif responce == -1:
                higher = nextGuess - 1
            else:
                lower = nextGuess + 1
        return lower


def guess(num):
    global pick
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(f"n = {solution.guessNumber(2)} pick = {pick}")
    print(f"n = {solution.guessNumber(1)} pick = {pick}")
    print(f"n = {solution.guessNumber(10)} pick = {pick}")
