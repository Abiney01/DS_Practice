from typing import List

# Mock MountainArray for testing (LeetCode provides this internally)
class MountainArray:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.calls = 0  # to track get() calls if needed

    def get(self, index: int) -> int:
        self.calls += 1
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # -------- 1. Find peak --------
        l, r = 1, n - 2
        while l <= r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)
            left_val = mountainArr.get(mid - 1)
            right_val = mountainArr.get(mid + 1)

            if left_val < mid_val < right_val:
                l = mid + 1
            elif left_val > mid_val > right_val:
                r = mid - 1
            else:
                peak = mid
                break

        # -------- 2. Binary search left (ascending part) --------
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid

        # -------- 3. Binary search right (descending part) --------
        l, r = peak + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val < target:
                r = mid - 1
            elif val > target:
                l = mid + 1
            else:
                return mid

        return -1

def run_tests():
    sol = Solution()

    tests = [
        ([1, 2, 3, 4, 5, 3, 1], 3),
        ([0, 1, 2, 4, 2, 1], 3),
        ([1, 5, 2], 2),
        ([1, 3, 5, 4, 2], 4),
        ([1, 2, 3, 4, 5, 3, 1], 6)
    ]

    for arr, target in tests:
        mountain = MountainArray(arr)
        result = sol.findInMountainArray(target, mountain)
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Index Found: {result}")
        print(f"get() calls: {mountain.calls}")
        print("-" * 40)


run_tests()
