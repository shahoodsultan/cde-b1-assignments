# Use a for loop to count the number of occurrences of the word in the list and return all indices where the word occurs.

def find_word_occurrences(words, search_word):
    count = 0
    indices = []
    for i, word in enumerate(words):
        if word == search_word:
            count += 1
            indices.append(i)
    print(f"'{search_word}' found {count} times at indices: {indices}")

find_word_occurrences(['apple', 'banana', 'apple', 'cherry', 'apple'], 'apple')


# ********************************************************************************************************

# Create a program to find all unique pairs of numbers in a list that add up to a target sum.
# Use a single list and a for loop (nested if necessary) to iterate through and find pairs without duplicates. Avoid repeating pairs like [3, 5] and [5, 3].

def find_pairs(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    print(pairs)

find_pairs([2, 4, 3, 5, 7, 8, 1], 9)

# ********************************************************************************************************

# Write a program to calculate the cumulative product of elements in a list.
# Use a single list and update it in place to store the cumulative product at each index. Use only a for loop.


def cumulative_product(numbers):
    for i in range(1, len(numbers)):
        numbers[i] *= numbers[i - 1]
    print(numbers)

cumulative_product([2, 3, 4, 5])

# ********************************************************************************************************

# Write a program to reshape a 1D list into a 2D grid.
# Accept a list of numbers and the number of rows as input. Use for loops to split the list into sublists, each representing a row. If the list cannot be evenly divided into rows, pad it with None.

def reshape_list(numbers, rows):
    result = []
    cols = -(-len(numbers) // rows)  
    for i in range(rows):
        start = i * cols
        end = start + cols
        row = numbers[start:end]
        while len(row) < cols:
            row.append(None)
        result.append(row)
    print(result)

reshape_list([1, 2, 3, 4, 5, 6, 7], 3)

# ********************************************************************************************************

# Write a program to sort a list of numbers into two separate lists:
# One list for all odd numbers (in ascending order). One list for all even numbers (in descending order). Use for loops for the entire process.

def sort_odd_even(numbers):
    odd = sorted([x for x in numbers if x % 2 != 0])
    even = sorted([x for x in numbers if x % 2 == 0], reverse=True)
    print(f"Odd: {odd}")
    print(f"Even: {even}")

sort_odd_even([5, 8, 3, 10, 2, 7, 1, 6])


# ********************************************************************************************************

# Write a program that uses a for loop to count the frequency of each character in a given string and stores the result in a dictionary.
# The program should ignore spaces and be case-insensitive. Display the dictionary as the final output.

def char_frequency(text):
    frequency = {}
    for char in text.lower():
        if char != ' ':
            frequency[char] = frequency.get(char, 0) + 1
    print(frequency)

char_frequency("Programming is fun")
