# Sliding Window Technique

# This is used in:

# substring problems
# subarray problems
# maximum/minimum length problems
# frequency-based questions

# Maintain a range (window) and adjust it dynamically instead of recomputing everything

# Problem 1: Max Sum Subarray of Size K
arr = [2, 1, 5, 1, 3, 2]
k = 3

# Brute Force
# Check all subarrays of size k → O(n*k)


def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]        # add next
        window_sum -= arr[i - k]    # remove previous
        
        max_sum = max(max_sum, window_sum)

    return max_sum


print(max_sum_subarray(arr, k))  # 9
# Dry Run
# Initial window: [2,1,5] = 8
# Slide:

# remove 2, add 1 → 6
# remove 1, add 3 → 9
# remove 5, add 2 → 6


# Problem 2: Longest Substring Without Repeating Characters

s = "abcabcbb"

# Idea (Variable Window)
# Use two pointers (left, right)
# Use set to track characters
# Expand right
# If duplicate → shrink left

def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_unique_substring(s))  # 3

# Dry Run
# Window expands:

# a → ab → abc
# Then duplicate 'a' comes → shrink from left