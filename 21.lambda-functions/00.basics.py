'''
syntax: (part-1)  (part-2)  (part-3)
         lamdba   param(s) operation
         lambda    num:     num ** 2

useful: when we need to pass a simple helper function to higher order function (a function which takes another function as argument)
'''

####

# 1. Write a lambda function that takes a number and returns its square. Assign it to a variable called square, and test it on the number 5.
square = lambda num: num**2
print(square(5))


# 2. Write a lambda function that takes two numbers and returns their product. Assign it to a variable multiply, and test it on the numbers 3 and 7.

multiply = lambda a,b: a*b 
print(multiply(3, 7))

'''
3. You are given a list of numbers:
nums = [1, 2, 3, 4, 5]
Use map() with a lambda function to double each number in the list. Convert the result to a list and print it.
'''
nums = [1, 2, 3, 4, 5]
doubled = map(lambda num:num*2, nums)
print(list(doubled))

'''
4. 
Use filter() and a lambda function to select only the words in this list that are longer than 4 characters:
words = ['hi', 'hello', 'sun', 'amazing', 'cat']
'''
words = ['hi', 'hello', 'sun', 'amazing', 'cat']
long_words = filter(lambda word: len(word) > 4, words) 
print(list(long_words))


"""
5. You are given a list of tuples, where each tuple contains a name and a score:
students = [('Alice', 88), ('Bob', 72), ('Charlie', 95)]
Use the sorted() function and a lambda to sort the list by score in descending order.
"""
students = [('Alice', 88), ('Bob', 72), ('Charlie', 95)]
# We tell sorted() to look at the second element (index 1) of each tuple
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
print(sorted_students)