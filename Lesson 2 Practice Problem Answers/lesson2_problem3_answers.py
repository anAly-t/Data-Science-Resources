# Practice Assignment 3: Word Frequency Counter
# Import the string module for working with punctuation
import string

# Function to count word frequencies in a given text
def word_frequency_counter(text):
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Remove punctuation and convert the text to lowercase
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()

    # Split the text into words
    words = text.split()

    # Iterate through each word and update the word frequency dictionary
    for word in words:
        # Use get() to retrieve the current frequency or default to 0 if the word is not in the dictionary
        word_freq[word] = word_freq.get(word, 0) + 1

    # Sort the word frequencies in descending order based on frequency
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Display word frequencies in descending order
    print("\nWord Frequencies:")
    for i, (word, freq) in enumerate(sorted_word_freq, 1):
        print(f"{i}. {word}: {freq}")

# Main execution block
if __name__ == "__main__":
    # Prompt the user to enter a text
    user_text = input("Enter a text: ")

    # Call the word_frequency_counter function with the user-provided text
    word_frequency_counter(user_text)
