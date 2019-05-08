# Write a function to remove the consecutive upper/lower and lower/upper case characters
# eg. Cc Dd cC dD

# Input: abcCkDdppGGa  -> abkppGGa
# Input: abCcBk        -> abBk

# Level: Hard

def remove_consecutive(string):
    result_string = ""
    duplicate = ""
    enum = enumerate(string)
    length = len(string) - 1

    for index, char in enum:
        if duplicate:
            if abs(ord(char) - ord(duplicate)) == 32:
                duplicate = char
                continue


        if index != length:
            next_char = string[index + 1]

            if abs(ord(char) - ord(next_char)) == 32:
                duplicate = char
                continue

        result_string += char

    return result_string

print(remove_consecutive("cC"))
