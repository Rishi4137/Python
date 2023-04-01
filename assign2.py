#1.Program to find the sum of all even numbers in a group of n numbers entered by the user. 
nums = []
n=int(input("Enter the number of elements in the list"))
print("Enter the elements for the list: ")
for i in range(n):
    val = int(input())
    nums.append(val)

sum = 0

for i in range(n):
    if nums[i]%2 == 0:
        sum = sum + nums[i]

print("\nSum of Even Numbers is", sum)


#2. Program to read a string and remove the given words from the string.
input_str = input("Enter the input string: ")

remove_list_str = input("Enter the list of words to remove (comma-separated): ")
remove_list = remove_list_str.split(',')

words_list = input_str.split()

for word in remove_list:
    while word in words_list:
        words_list.remove(word)

output_str = ' '.join(words_list)

print("Output string:", output_str)

#3.Find the average word length of a sentence 

sentence = input("Enter a sentence: ")

words = sentence.split()
total_length = 0
num_words = len(words)

for word in words:
    total_length += len(word)

average_length = total_length / num_words

print("The average word length in the sentence is:", average_length)

# 5. Program to remove all duplicate elements from a list
my_list = [1, 2, 3, 4, 2, 3, 5, 1]

unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("Original list:", my_list)
print("List with duplicates removed:", unique_list)

#6.Consider a list consisting of integers, floating point numbers and strings. Separate them into different lists depending on the data

mixed_list = [1, 2.5, "hello", 3, "world", 4.2, 5, "Python"]

int_list = []
float_list = []
str_list = []

for element in mixed_list:
    if isinstance(element, int):
        int_list.append(element)
    elif isinstance(element, float):
        float_list.append(element)
    elif isinstance(element, str):
        str_list.append(element)

print("List of integers:", int_list)
print("List of floating-point numbers:", float_list)
print("List of strings:", str_list)

#7. Write a Python program to read list of positive integers and separate the prime and composite numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num_list = []
while True:
    num_str = input("Enter a positive integer (or 'done' to finish): ")
    if num_str == "done":
        break
    num = int(num_str)
    if num < 1:
        raise ValueError
    num_list.append(num)
    
prime_list = []
composite_list = []

for num in num_list:
    if is_prime(num):
        prime_list.append(num)
    else:
        composite_list.append(num)

print("Prime numbers:", prime_list)
print("Composite numbers:", composite_list)


#8. Write a Python program to read a list of numbers and sort the list in a nondecreasing order without using any built in functions. Separate function should be written to sort the list wherein the name of the list is passed as the parameter

def sort_list(my_list):
    n = len(my_list)
    for i in range(n):
        for j in range(i+1, n):
            if my_list[j] < my_list[i]:
                my_list[i], my_list[j] = my_list[j], my_list[i]

num_list = []
while True:
    num_str = input("Enter a number (or 'done' to finish): ")
    if num_str == "done":
        break
    try:
        num = float(num_str)
        num_list.append(num)
    except ValueError:
        print("Invalid input, please enter a number")

sort_list(num_list)

print("Sorted list:", num_list)


#9. Check if the items in the list are sorted in ascending or descending order and print suitable messages accordingly. Otherwise, print “Items in list are not sorted”

num_list = []
while True:
    num_str = input("Enter a number (or 'done' to finish): ")
    if num_str == "done":
        break
    try:
        num = float(num_str)
        num_list.append(num)
    except ValueError:
        print("Invalid input, please enter a number")

is_ascending = all(num_list[i] <= num_list[i+1] for i in range(len(num_list)-1))

is_descending = all(num_list[i] >= num_list[i+1] for i in range(len(num_list)-1))

if is_ascending:
    print("Items in list are sorted in ascending order")
elif is_descending:
    print("Items in list are sorted in descending order")
else:
    print("Items in list are not sorted")


#10. Write a python code to input n numbers and calculate sum of cubes of each number and store it in a list.
n = int(input("Enter the number of numbers to input: "))

sum_of_cubes_list = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    sum_of_cubes = num**3
    sum_of_cubes_list.append(sum_of_cubes)

print("List of sums of cubes:", sum_of_cubes_list)
