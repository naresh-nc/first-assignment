#Task 2: Control Flow (if/else)

# Write a program that takes a number as input.
# Use an if/else statement to determine if the number is even or odd and print the result.


number = int(input("Enter a number: "))


if number % 2 == 0:
  print(f"{number} is even.")

else:
  print(f"{number} is odd.")