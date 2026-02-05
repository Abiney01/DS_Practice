class GuessGame:
    def __init__(self, pick):
        self.pick = pick

    def guess(self, num: int) -> int:
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else:
            return 0


class Solution(GuessGame):
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            res = self.guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1

game = Solution(pick=6)
print(game.guessNumber(10))
