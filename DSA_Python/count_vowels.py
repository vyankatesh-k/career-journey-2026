def count_vowels_brute(s):
    """
    Brute force approach using multiple OR conditions.
    Time Complexity: O(n)
    """
    count = 0
    for ch in s.lower():
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
    return count


def count_vowels_membership(s):
    """
    Optimized approach using membership check in string.
    Time Complexity: O(n)
    """
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count


def count_vowels_set(s):
    """
    Best practice using set for constant-time lookup.
    Time Complexity: O(n)
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count


def count_vowels_pythonic(s):
    """
    Pythonic one-liner approach.
    Time Complexity: O(n)
    """
    return sum(1 for ch in s.lower() if ch in "aeiou")


if __name__ == "__main__":
    s = "education"

    if not s:
        print("Vowel Count: 0")
    else:
        print("Brute Force:", count_vowels_brute(s))
        print("Membership Check:", count_vowels_membership(s))
        # All approaches run in O(n), but using a set is preferred for constant-time lookup and better readability.
        print("Set Approach:", count_vowels_set(s))
        print("Pythonic:", count_vowels_pythonic(s))

