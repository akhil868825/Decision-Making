...
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
...
def check_character(char):
    vowels = "aeiouAEIOU"
    
    if char.isalpha():  # Check if the character is an alphabet
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Not an alphabet"

# Input format
char = input("Enter a character: ")

# Check the character and get the result
result = check_character(char)

# Output format
print(result)
