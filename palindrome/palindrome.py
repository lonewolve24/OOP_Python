class Palindrome:
    def __init__(self, word):
        self.word = word

    def is_palindrome(self):
        clean_word = self.word.lower()
        
        # Remove non-alphanumeric characters (e.g., spaces, punctuation)
        clean_word = ''.join(char for char in clean_word if char.isalnum())
        # Revers non-alphnumeric charaters
        reverse = clean_word[::-1]
         #compare the word with the reversed word
        if  clean_word == reverse:
            return True
        else:
            return False

# Example usage:


if __name__ == '__main__':
    while True:
        user_input  = str(input("Enter a Word\n ----->"))

        if user_input.lower() == "quit":
            break
        word1  = Palindrome( user_input)

        if word1.is_palindrome():
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"'{user_input}' is not a palindrome.")
    