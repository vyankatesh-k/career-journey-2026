def reverse_string_brute(s):
    """
    Reverse string using backward traversal.
    Time Complexity: O(n²) due to string concatenation
    """
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str


def reverse_string_list(s):
    """
    Reverse string using list and join.
    Time Complexity: O(n)
    """
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    return "".join(result)


def reverse_string_two_pointer(s):
    """
    Reverse string using two-pointer technique.
    Time Complexity: O(n)
    """
    arr = list(s)
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return "".join(arr)


def reverse_string_pythonic(s):
    """
    Python built-in slicing.
    Time Complexity: O(n)
    """
    return s[::-1]


if __name__ == "__main__":
    s = "python"

    if not s:
        print("Reversed: ")
    else:
        print("Brute Force:", reverse_string_brute(s))
        print("List Approach:", reverse_string_list(s))
        print("Two Pointer:", reverse_string_two_pointer(s))
        print("Pythonic:", reverse_string_pythonic(s))