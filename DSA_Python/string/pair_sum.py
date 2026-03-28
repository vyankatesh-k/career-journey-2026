# Pair with Given Sum
arr = [2, 3, 5, 8, 11]
target = 10

# O/p: [2, 8]

# Thinking Process
# Start from both ends
# Calculate sum

# If sum is:
#   too small → move left++
#   too big → move right--
#   equal → done

def find_pair(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]
        
        elif current_sum < target:
            left += 1
        
        else:
            right -= 1

    return None


print(find_pair([2, 3, 5, 8, 11], 10))  # (2, 8)

# Common Mistakes
# Using nested loops
# Forgetting array must be sorted
# Moving both pointers incorrectly