# main.py

from text_processing_tool import count_words, find_unique_words, convert_to_uppercase

# Prompt the user to enter a text string
text = input("Enter a text string: ")

# Process the text based on user input
word_count = count_words(text)
unique_words = find_unique_words(text)
uppercase_text = convert_to_uppercase(text)

# Print the results
print(f"Word count: {word_count}")
print(f"Unique words: {unique_words}")
print(f"Uppercase text: {uppercase_text}")
