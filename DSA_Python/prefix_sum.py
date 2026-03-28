# What is Prefix Sum?
# Instead of calculating sum again and again, we precompute cumulative sums

# Create an array where:
# prefix[i] = sum of elements from index 0 to i

# arr = [2, 4, 1, 3]
# Prefix Array: [2, 6, 7, 10]

#  Brute Force
# sum(arr[L:R+1])   # O(n)

# Prefix Sum
# sum(L → R) = prefix[R] - prefix[L-1] # O(1)

Problem 1: Range Sum Query

# arr = [2, 4, 1, 3, 5]
# Query: L = 1, R = 3
# Output: 4 + 1 + 3 = 8

def build_prefix(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix


def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    return prefix[R] - prefix[L-1]


arr = [2, 4, 1, 3, 5]
prefix = build_prefix(arr)

print(range_sum(prefix, 1, 3))  # 8

# Complexity:
# Build: O(n)
# Query: O(1)

# Problem 2: Count Subarrays with Given Sum (Intro)
# arr = [1, 2, 3]
# target = 3

# Subarrays:
# [1,2]
# [3]

# Output: 2

# Instead of checking all subarrays: Use prefix sum + hashmap

def count_subarrays(arr, target):
    prefix_sum = 0
    count = 0
    hashmap = {0: 1}

    for num in arr:
        prefix_sum += num

        if prefix_sum - target in hashmap:
            count += hashmap[prefix_sum - target]

        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count


print(count_subarrays([1, 2, 3], 3))  # 2

# Complexity:
# Time: O(n)
# Space: O(n)


# Common Mistakes

# Forgetting L == 0 case
# Not initializing hashmap {0:1}
# Off-by-one errors
