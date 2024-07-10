# Use a for loop to iterate over the elements in a list of numbers and print each number multiplied by 2.
# Use a while loop to calculate the sum of numbers from 1 to 10.


# for loop - multiply by 2
numbers = [1, 2, 3, 4, 5]

for x in numbers:
  doubled_number = x * 2
  print(f"{x} x 2 = {doubled_number}")


  # while loop - sum of numbers 1 to 10
total_sum = 0
current_number = 1

while current_number <= 10:
  total_sum += current_number
  current_number += 1

print(f"Sum of numbers from 1 to 10: {total_sum}")