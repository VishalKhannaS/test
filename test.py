print('hello world 1')
"""
This script prints 'hello world 1' and then generates a list of odd numbers from 1 to 100.
Functions:
    None

    odd_numbers (list): A list to store odd numbers from 1 to 100.
The script performs the following steps:
1. Prints 'hello world 1'.
2. Initializes an empty list called `odd_numbers`.
3. Iterates through numbers from 1 to 100.
4. Checks if the number is odd.
5. If the number is odd, appends it to the `odd_numbers` list.
6. Prints the list of odd numbers.
"""
# write a code to print 10 numbers

def generate_odd_numbers():
    odd_numbers = []
    for i in range(1, 101, 2):
        odd_numbers.append(i)
    return odd_numbers

odd_numbers = generate_odd_numbers()

print(odd_numbers)
