from collections import defaultdict
import bisect

N = int(input('кол-во чисел '))
nums = [int(input('число ')) for i in range(N)]
target = int(input('цель '))
def func(nums, target):
    n = len(nums)
    closest_sum = float('inf')
    closest_combination = []

    sum_pairs = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            current_sum = nums[i] + nums[j]
            sum_pairs[current_sum].append((i, j))

    # O(N^2)

    sorted_pair_sums = sorted(sum_pairs.keys())

    # O(N)

    for i in range(n):
        for j in range(i + 1, n):
            curent_sum = nums[i] + nums[j]
            r_sum = target - curent_sum

            idx = bisect.bisect_left(sorted_pair_sums, r_sum)

            candidates = []

            if idx != len(sorted_pair_sums):
                candidates.append(sorted_pair_sums[idx])
                if sorted_pair_sums[idx] == r_sum and idx + 1 < len(sorted_pair_sums):
                    candidates.append(sorted_pair_sums[idx + 1])

            if idx > 0:
                candidates.append(sorted_pair_sums[idx - 1])

            for pair_sum in candidates:
                for k, l in sum_pairs[pair_sum]:
                    if i != k and i != l and j != k and j != l:
                        total_sum = pair_sum + curent_sum

                        if abs(total_sum - target) < abs(closest_sum - target):
                            closest_sum = total_sum
                            closest_combination = [nums[i], nums[j], nums[k], nums[l]]

    # O(N^2)*O(logN)*O(3)*O(K) = O(logN*N^2)

    return closest_combination, closest_sum
print(func(nums,target))