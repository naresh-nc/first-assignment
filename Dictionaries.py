#Task 6: Dictionaries

# Create a dictionary to store information about a book (title, author, year).
# Access and print individual values from the dictionary.
# Add a new key-value pair to the dictionary (e.g., genre).
# Use a loop to iterate over the dictionary's items and print them.


# Book information
book_title = "Pride and Prejudice"
book_author = "Jane Austen"
book_year = 1813

# Printing Book information
book_info = {
  "Title": book_title,
  "Author": book_author,
  "Year Published": book_year
}

print(f" {book_info}")


# Add a new piece of information (like putting a new item in the box)
book_info["Genre"] = "Romance"

# Print all information together (like looking at everything in the box)
for key, value in book_info.items():
  print(f"{key}: {value}")