# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def is_unique_characters(string):
    if len(string) > 128:
        return False

    # Initialise null value byte array of ASCII length
    bool_array = bytearray(128)

    for c in string:
        # Get ASCII value of character
        val = ord(c)

        if bool_array[val]:
            # Already found this character in string
            return False

        bool_array[val] = 1

    return True


print(is_unique_characters("asdflkj"))
print("")
print(is_unique_characters("asdfsdljfslifj"))
