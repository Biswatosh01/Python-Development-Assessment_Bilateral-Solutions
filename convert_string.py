# 1. Write a Python function that takes a string as input and reverses it but with a twist: every vowel in the reversed string should be capitalized, and every consonant should be converted to lowercase. For example, if the input is "Hello, World!", the output should be "!dLrOw ,oLlEh".

def reverse_and_convert(s: str) -> str:
    vowels = 'aeiou'
    reversed_string = s[::-1]
    converted_string = ''

    for char in reversed_string:
        if char.lower() in vowels:
            converted_string += char.upper()
        else:
            converted_string += char.lower()

    return converted_string

input_string = input("Enter the input string: ")
output_string = reverse_and_convert(input_string)
print(output_string)
