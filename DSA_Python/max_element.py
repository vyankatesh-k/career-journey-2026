# Finding the largest number 
# arr = [3, 7, 2, 9, 5] 
# import time 
# import random 

# arr = [random.randint(1, 100000) for _ in range(10000)] 
# arr = [random.randint(1, 100000) for _ in range(50000)] 

# For worst case-scenario: Largest is at end 
arr = list(range(1, 10001)) # strictly increasing 

if not arr: 
    print("Empty array") 
    exit() 
    
# ------------------------------- 
# Brute Force Approach 
# ------------------------------- 
start = time.perf_counter() 
max_brute = None 

for i in range(len(arr)):
    is_max = True
    for j in range(len(arr)):
        if arr[j] > arr[i]:
            is_max = False
            break
    if is_max:
        max_brute = arr[i]
        break
        
is_max = True 
for j in range(len(arr)): 
    if arr[j] > arr[i]: 
        is_max = False 
        break 
    if is_max: 
        max_brute = arr[i]
        break
    
end = time.perf_counter() 
print("Brute Max:", max_brute) 
print("Brute Time:", end - start) 


# ------------------------------- 
# Optimized Approach 
# ------------------------------- 
start = time.perf_counter() 

max_val = arr[0] 
for num in arr: 
    if num > max_val: 
        max_val = num 
        
end = time.perf_counter() 

print("Optimized Max:", max_val) 
print("Optimized Time:", end - start) 

# Using Built-ins 
print(max(arr)) 
# Conceptually it works over Optimized solution only 
# max_val = first_element 
# for each element: 
# if element > max_val: 
# max_val = element 
# return max_val 

print(max("python")) # 'y' 
print(max([1, 5, 2])) # 5 

arr2 = ["apple", "banana", "kiwi"] 
print(max(arr2, key=len)) # banana