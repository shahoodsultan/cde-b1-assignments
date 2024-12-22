# Write a function called create_word_count that takes a list of strings and returns a dictionary where:
# Keys are unique words from the list. Values are the count of occurrences of each word.

def create_word_count(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print(word_count)

create_word_count(['apple' , 'banana' , 'mango' , 'apple' , 'banana' , "chery"])



# **************************************************************************************
     
# Write a function called sort_by_key that takes a list of dictionaries and a key to sort by.
# The function should return a new list sorted by the given key in ascending order. If the key doesn’t exist in a dictionary, ignore that dictionary.

def sort_by_key(data, key):
    sorted_data = sorted([d for d in data if key in d], key=lambda x: x[key])
    print(sorted_data)

data = [{'name': 'Saad', 'age': 21}, {'name': 'Usama', 'age': 22}, {'name': 'Umar', 'age': 20}]
sort_by_key(data, 'age')



# **************************************************************************************

# Write a function called filter_dict that takes a dictionary and a value threshold as arguments.
# The function should return a new dictionary containing only the key-value pairs where the value is greater than the threshold.

def filter_dict(d, threshold):
    filtered = {k: v for k, v in d.items() if v > threshold}
    print(filtered)

filter_dict({'Saad': 92, 'Usama': 80, 'Umar': 88, 'Muhammad': 72}, 70)

# **************************************************************************************
     
# Write a function called find_common_keys that takes two dictionaries and returns a list of keys that are common to both.

def find_common_keys(dict1, dict2):
    common_keys = list(dict1.keys() & dict2.keys())
    print(common_keys)

find_common_keys({'a': 1, 'b': 2, 'c': 3}, {'b': 4, 'c': 5, 'd': 6})



# **************************************************************************************
     
# Write a function called update_grades that takes a list of dictionaries (representing students with their grades) and updates the grade of a student if their name matches the given name.

def update_grades(students, name, new_grade):
    for student in students:
        if student['name'] == name:
            student['grade'] = new_grade
    print(students)

update_grades([{'name': 'Saad', 'grade': 95}, {'name': 'Usama', 'grade': 90}], 'Umar', 95)


# **************************************************************************************
     
# Write a function called merge_lists_to_dict that takes two lists of equal length:
# The first list contains keys. The second list contains values. The function should return a dictionary created by merging these lists.

def merge_lists_to_dict(keys, values):
    merged_dict = dict(zip(keys, values))
    print(merged_dict)

merge_lists_to_dict(['name', 'age', 'city'], ['Saad', 21, 'New Karachi'])



     