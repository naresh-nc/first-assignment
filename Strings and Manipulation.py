# Create a string variable containing a sentence.
# Use string methods to:
# Convert the sentence to uppercase and lowercase.
# Split the sentence into a list of words.
# Find the length of the sentence.
# Replace a specific word in the sentence with another word.



# Create a string sentence
sentence = "This is a test sentence."

# Uppercase and lowercase
uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()

# Split into words (list)
words = sentence.split()

# Length of the sentence
sentence_length = len(sentence)

# Replace a word
new_sentence = sentence.replace("test", "replaced")

# Print results
print(f"Original sentence: {sentence}")
print(f"Uppercase: {uppercase_sentence}")
print(f"Lowercase: {lowercase_sentence}")
print(f"Words as list: {words}")
print(f"Length of sentence: {sentence_length}")
print(f"Sentence with replaced word: {new_sentence}")