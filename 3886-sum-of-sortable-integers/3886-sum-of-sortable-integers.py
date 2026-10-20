class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0
        target = sorted(nums)

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for i in range(0, n, k):
                arr = nums[i:i + k]
                m = len(arr)

                drops = 0
                for j in range(m):
                    if arr[j] > arr[(j + 1) % m]:
                        drops += 1

                if drops > 1:
                    valid = False
                    break

            if valid:
                result = []
                for i in range(0, n, k):
                    arr = nums[i:i + k]
                    drops = [j for j in range(k) if arr[j] > arr[(j + 1) % k]]

                    if drops:
                        p = (drops[0] + 1) % k
                        arr = arr[p:] + arr[:p]

                    result.extend(arr)

                if result == target:
                    ans += k

        return ans