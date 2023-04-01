#1. Program to display the frequency of each word in a given string.

def word_frequency(string):
    frequencies = {}
    words = string.split()
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    for word, count in frequencies.items():
        print(f"{word}: {count}")

string1=input("Enter a string")
word_frequency(string1)


#2. Write a Python program to create a dictionary of roll numbers and names of five students. Display the names in the dictionary in alphabetical order.

students = {
    101: 'Abiram',
    102: 'Benny',
    103: 'Catherine',
    104: 'David',
    105: 'Evena'
}

names = sorted(students.values())

print("Names of students in alphabetical order:")
for name in names:
    print(name)

#3. Program to read name and phn numbers of ‘n’ customers and print the list in sorted order of names

n = int(input("Enter the number of customers: "))

customers = {}
for i in range(n):
    name = input("Enter the name of customer {}: ".format(i+1))
    phone = input("Enter the phone number of customer {}: ".format(i+1))
    customers[name] = phone
sorted_names = sorted(customers.keys())

print("List of customers in alphabetical order:")
for name in sorted_names:
    print("{} - {}".format(name, customers[name]))

#4. In the above program after printing the sorted list, read a name and delete that customer from the dictionary if present.
n = int(input("Enter the number of customers: "))

customers = {}
for i in range(n):
    name = input("Enter the name of customer {}: ".format(i+1))
    phone = input("Enter the phone number of customer {}: ".format(i+1))
    customers[name] = phone
sorted_names = sorted(customers.keys())

print("List of customers in alphabetical order:")
for name in sorted_names:
    print("{} - {}".format(name, customers[name]))
delete_name = input("Enter the name of the customer to delete: ")

# Check if the customer exists in the dictionary
if delete_name in customers:
    # Delete the customer from the dictionary
    del customers[delete_name]
    print("{} has been deleted from the list of customers.".format(delete_name))
else:
    print("{} is not in the list of customers.".format(delete_name))
#5.  program uses a dictionary to convert hexadecimal number into binary.

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
hex_num = input("Enter a hexadecimal number: ")
binary_num = ''.join([hex_to_bin[ch] for ch in hex_num])
print("The binary equivalent of {} is {}".format(hex_num, binary_num))

#6. Finding the mode of list of numbers

numbers = [2, 5, 3, 2, 4, 5, 2, 3, 5, 3, 3]
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
mode = max(freq, key=freq.get)
print("The mode of the list is:", mode)

#7. A matrix which contains large number of zeros is called sparse matrix. A better way to represent sparse matrix is my storing only the non zero element and its index using a dictionary.
sparse_matrix = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 3, 0, 0, 4]
]
sparse_dict = {}
for i in range(len(sparse_matrix)):
    for j in range(len(sparse_matrix[i])):
        if sparse_matrix[i][j] != 0:
            sparse_dict[(i, j)] = sparse_matrix[i][j]

print("Sparse matrix as dictionary:")
print(sparse_dict)


#8. Write a Python code to create a function called list_of_frequency that takes a string and prints the letters in non-increasing order of the frequency of their occurrences. Use dictionaries.
def list_of_frequency(string):
    freq = {}
    
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    sorted_keys = sorted(freq, key=freq.get, reverse=True)
    
    for key in sorted_keys:
        print(key, freq[key])

#9. Write a Python program to combine two dictionary adding values for common keys. d1 = {'a':10, 'b': 20, 'c':30} d2 = {'a': 30, 'b': 20, 'd':40} Sample output: {'a': 40, 'b': 40, 'd': 40, 'c': 30}
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}
 
 for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass
         
print(dict2)