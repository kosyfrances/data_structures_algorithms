# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# string1 = ABCB
# string2 = BABC
# ABC != "BAC    "

# str1 = {"A": 1, "B": 3, "C": 1}

def is_perm(str1, str2):
    # length must be equal
    if len(str1) != len(str2):
        return False

    str1_map = {}

    # O(n)
    for char in str1:
        # O(m)
        if char not in str1_map:
            str1_map[char] = 1
        else:
            str1_map[char] += 1

    for char in str2:
        if char not in str1_map:
            return False
        if char in str1_map and str1_map.get(char) == 0:
            return False
        str1_map[char] -= 1

    return True

print(is_perm("ABCBB", "BABCB"))
