# Python Basics

![Python](images/python_icon.png)

---
# What is Python?
* Scripting language
* Object Orientated
* 1.0 released Jan, 1994
* 3.0 released Dec, 2008

---
# Differences to Java
* Dynamic Typing
* Indentation
* Slower at runtime
* Faster to develop
* Batteries included
* Easier to learn*

---
# Python on Linux
* Usually preinstalled
* Will use Python3 in this course
* Run a Python:
`
python3 program.py
`
* Can install [iPython](http://ipython.readthedocs.io/en/stable/) for a nicer REPL

---
# Data Types
* Boolean - `bool`
* Numeric - `int` `float` `complex`
* Sequences - `str` `list`* `tuple`
* Sets - `set`*
* Maps - `dict`*
* None - null object

\* - mutable data types

---
# Strings
* String literals can be written in a variety of ways
    - Singe quotes - `'allows embedded "double" quotes'`
    - Double quotes - `"allows embedded 'single' quotes"`
    - Triple quotes - `'''Can span multiple lines'''`
* Strings are immutable
* Concatenate strings using `+`

<!-- -->

    !python
    'hello ' + 'world'

---
# Input/Output
* Input using the `input(prompt)` function
* Output using the `print(value)` function

<!-- -->
    !python
    username = input('Enter your username here: ')
    balance = input('Enter the balance here: ')

    print('Welcome {}, your balance is {}'.format(username, balance))

---
# String Interpolation

    !python
    print('Hello {}, my name is {}'.format('world', 'Tom'))

    # Specify named arguments
    print('Welcome {user}, today is {day}'.format(user='Mary', day='Wednesday'))

    # Specify positional arguments
    print('{2} {0} {1} {2}'.format('a', 'b', 'c'))

    # Formatting floats to 2 decimal places
    print('{:.2f}'.format(99.23456))
    
<!-- -->
    'Hello world, my name is Tom'
    'Welcome Mary, today is Wednesday'
    'c a b c'
    '99.23'

---
# String methods

    !python
    print('programming in python'.split(' '))

    print('programming in python'.title())

    print('programming was fun'.replace('was', 'is'))

    print('abc def'.upper())

    print('abc' * 2)

<!-- -->
    ['programming', 'in', 'python']
    'Programming in Python'
    'programming is fun'
    'ABC DEF'
    'abcabc'

---
# Integers & Floats
* Can cast objects to other types

<!-- -->
    !python
    s = '17.89'

    # Cast the string to a float
    f = float(s)

    # Cast the float to an int (rounds down)
    i = int(f)

    print(f)
    print(i)

<!-- -->

    17.89
    17

---
# Casting - ValueError
* A ValueError exception will be raised if the object cannot be cast to the specified type

<!-- -->
    !python
    int('17.89')
    float('a')

<!-- -->
    ValueError: invalid literal for int() with base 10: '17.89'
    ValueError: could not convert string to float: 'a'

---
# Math Functions
* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division
* `%` Modulo
* `**` Power of

And much more in the [math standard library](https://docs.python.org/3.2/library/math.html#module-math)

---
# Exercise - Math Program
* Write a program that:
    - Takes two floats from stdin input
    - Prints the following results for the two numbers:
        + addition
        + subtraction
        + multiplication
        + division
        + modulo
        + power of

Sample input & output on next slide

---
# Exercise - Math Program
* Sample Input

<!-- -->
    8
    4

* Sample Output

<!-- -->
    8.0 plus 4.0 equals 12.0
    8.0 minus 4.0 equals 4.0.0
    8.0 multiplied by 4.0 equals 32.0
    8.0 divided by 4.0 equals 2.0
    8.0 modulo 4.0 equals 0.0
    8.0 to the power of 4.0 equals 4096.0

---
# Boolean Expressions
* Two boolean types - False & True
* Can be used with boolean operators
* All of these expressions evaluate to `True`

<!-- -->

    !python
    True and True
    False or True
    not False

---
# Comparison Operations
* Compare the values of two object
* The objects do not need to have the same type, but they must be orderable against each other

<!-- -->

    !python
    x < y
    x > y
    x == y
    x >= y
    x <= y
    x != y

    # Compare if two variables point to the same object
    x is y
    x is not y

    # Determine if a value is in a collection
    x in collection
    x not in collection

---
# If / Else Statements
* `if` statements do not require the condition be surrounded by brackets
* The `elif` and `else` are optional. Can just have a single `if` condition and statement

<!-- -->
    !python
    x = 3

    if x < 2:
        print('Small x')
    elif x < 4:
        print('Medium x')
    else:
        print('Large x')

<!-- -->
    Medium x

---
# Boolean Expressions - Truthy & Falsey
* Other types can be used in a boolean context
* The following values are considered False:
    - `0`
    - `None`
    - Empty strings - `""`
    - Empty collections - `{}, [], ()`

---
# Boolean Expressions - Truthy & Falsey

    !python
    s = 'my string'
    if s:
        print('this string is not empty: {}'.format(s))
    else:
        print('this string is empty')

<!-- -->

    this string is not empty: my string

---
# Exercise - Logical Operations
* Write a program to take a word from a user
* If the word doesn't start with "t" or "T" then output a statement that it must
* If the word is shorter than 3 letters then output that it is too short
* If the word is longer than 6 letters then output that it is too long
* If all conditions are satisfied, then output that this is the case

Sample input & output on next slide

---
# Exercise - Logical Operations
***Note***: Input and output shown in the same code blocks below

<!-- -->
    carrot
    The word "carrot" does not start with "t"

<!-- -->
    to
    The word "to" is too short

<!-- -->
    telephone
    The word "telephone" is too long

<!-- -->
    tulip
    The word "tulip" satisfies this program!

<!-- -->
    Tulip
    The word "Tulip" satisfies this program!

---
# While Loops
* Continues to loop until the condition is `False`

<!-- -->
    !python
    import time

    print('Countdown...')

    time_left = 3
    while time_left > 0:
        print('{}..'.format(time_left))
        time_left = time_left - 1
        time.sleep(1)

    print('Take off!!')

<!-- -->
    Countdown...
    3...
    2...
    1...
    Take off!!

---
# For Loops
* `for` loops are used to iterate through a collection
* Declare the variable to hold the value of the element during each iteration

<!-- -->
    !python
    # Prints all even numbers in the list
    numbers = [8,2,3,7,10]

    for number in numbers:
        if number % 2 == 0:
            print(number)

<!-- -->
    8
    2
    10

---
# For Loops
* `for` loops can be used with any iterable type, including strings

<!-- -->
    !python
    for letter in "Hello World":
        if letter.isupper():
            print(letter)

<!-- -->
    H
    W

---
# Iterables
* Iterables are types that contain zero or more elements that can be iterated across
* Here are a subset of the most commonly used iterable types
    - Sequence Types
        + `list`
        + `str`
        + `tuple`
    - Non-sequence Types
        + `dict`
        + `set`
---
# Iterable Functions
* `len` - Get the size of the collection
* `in` - Determine if an element is in the collection

<!-- -->
    !python
    vowels = ('a', 'e', 'i', 'o', 'u')
    print('There are {} vowels'.format(len(vowels)))

    sentence = 'I eat apples in April' 
    print('The vowels in "{}" are:'.format(sentence), end=' ')
    for letter in sentence:
        # If the letter is in the vowel tuple
        if letter.lower() in vowels:
            print(letter, end=' ')

<!-- -->
    There are 5 vowels
    The vowels in "I eat apples in April" are: I e a a e i A i

***Note***: The `end=' '` parameter to print specifies that instead of printing a new line, just print a space

---
# Iterable Functions
* `for` and `in` work on the key in dicts

<!-- -->
    !python
    sample_words = {'a': 'apple', 'b': 'ball'}

    print('a' in sample_words)
    print('ball' in sample_words)

    for letter in sample_words:
        print('There is a word for "{}"'.format(letter))

<!-- -->
    True
    False
    There is a word for "a"
    There is a word for "b"

---
# Iterable Functions
* Use the `items()` method to get both key and value during the iteration

<!-- -->
    !python
    sample_words = {'a': 'apple', 'b': 'ball'}

    for letter, word in sample_words.items():
        print('A sample word for "{}" is "{}"'.format(letter, word))

<!-- -->
    A sample word for "a" is "apple"
    A sample word for "b" is "ball"

---
# Range
* The `range` object can be used to simulate a list of numbers

<!-- -->
    range(stop) -> range object
    range(start, stop[, step]) -> range object
```

* Type cast to `list` to view the 'contents' of the range

<!-- -->
    !python
    # From 3 to 10
    print(list(range(3,10)))

    # From 0 to 10, in steps of 2
    print(list(range(0,10,2)))

    # From 5 to 0, in steps of -1
    print(list(range(5,0,-1)))

<!-- -->
    [3, 4, 5, 6, 7, 8, 9]
    [0, 2, 4, 6, 8]
    [5, 4, 3, 2, 1]

---
# For Loops with Range

<!-- -->
    !python
    total = 0

    for i in range(5):
        total += i
    
    print(total)

<!-- -->
    10

---
# Loops - Control Flow
* Use `continue` & `break` to change the natural flow of a loop
* `continue` skips the rest of the current iteration and starts the next
* `break` terminates the loop

<!-- -->
    !python
    while True:
        should_quit = input('Quit: [Y/n] ')
        if should_quit == 'Y':
            break

        user = input('Username: ')
        if len(user) == 0:
            continue

        print('Welcome, {}'.format(user))

---
# Mutable Collections - Lists
* Create lists using the `[]` or `list` keywords

<!-- -->
    !python
    l = [2,4,6]

    # Append 7 to the end of the list
    l.append(7)

    # Insert 77 at the start of the list
    l.insert(0, 77)

    print(l)

<!-- -->

    [77, 2, 4, 6, 7]

---
# Mutable Collections - Lists
* Access an element of a list using the index number - 0th indexed
* Many useful methods on lists. `dir(list)` for a full listing

<!-- -->
    !python
    l = [1,8,1,2,9,2,1,9]

    l.sort()
    print('Sorted: {}'.format(l))

    print('The 3rd element in the list is {}'.format(l[2]))

    print("There are {} 1's in the list".format(l.count(1)))

    print('The min and max are {} and {}'.format(min(l), max(l)))

<!-- -->
    Sorted: [1, 1, 1, 2, 2, 8, 9, 9]
    The 3rd element in the list is 1
    There are 3 1's in the list
    The min and max are 1 and 9

---
# Mutable Collections - Sets
* Create sets using the `{}` or `set` keywords
* A set will only store each value once

<!-- -->
    !python
    # 3 will only be referenced once
    s = {3,4,5,3}

    s.add(2)
    s.remove(5)

    print(s)

<!-- -->
    {2, 3, 4}


---
# Mutable Collections - Dict
* Create dicts using the `{}` or `dict` keywords
* Overwrite and add entries using the `d[key]` syntax
* Delete entries by using the `del d[key]` syntax

<!-- -->
    !python
    d = {1: 2, 'foo': 'bar'}

    d[1] = 'hello'
    del d['foo']

    print(d)

<!-- -->
    {1: 'hello'}

---
# Exercise - Collections
* Write a program that takes a whitespace separated list of words
* Split the input string using the `str.split()` method
* Output a dict with integer keys and corresponding lists with all words of that length
* Sample Input

<!-- -->
    apple car movie hair more

* Sample Output

<!-- -->
    {3: ['car'], 4: ['hair', 'more'], 5: ['apple', 'movie']}

---
# For Comprehensions
* The `for` keyword can also be used in the generation of collections:
    - lists
    - sets
    - dicts
    - generators
* This is the idiomatic way to **transform / filter** collections in Python
* Use in combination with if statements to filter the collection
* Use in combination with functions to transform the collection

***Note***: If you do not care about the results of the for loop then you would still use a regular
for loop rather than a for comprehension

---
# For Comprehensions - Lists
    !python
    numbers = [3,9,2,1,10,4,2,7]

    # Transform - Get the squares
    squares = [v * v for v in numbers]

    # Filter - Only keep the even numbers
    evens = [v for v in numbers if v % 2]

    print(squares)
    print(evens)

<!-- -->
    [9, 81, 4, 1, 100, 16, 4, 49]
    [3, 9, 1, 7]

---
# For Comprehensions - Dicts
    !python
    words = ['sign', 'apple', 'baloon', 'dog', 'ball', 'sweet']

    # Create a map with a letter as key and the last word in the list
    # starting with that letter
    last_found = { w[0]: w for w in words }
    print(last_found)

<!-- -->
    {'a': 'apple', 'b': 'ball', 'd': 'dog', 's': 'sweet'}

---
# Dynamic vs Static Typing
* Staticically typed lanaguages
    - Compile time type checking
    - Variables have a declared type
* Dynamically typed languages
    - Run-time type checking
    - Variable is just a name

---
# Dynamic Typing

    !python
    # Variables are not constrained to the type they can point to
    x = 1
    print(x)
    x = 'hello world'
    print(x)

<!-- -->
    1
    hello world

---
# Everything is an Object
* View all the functions on the string object for example:

<!-- -->

    !python
    dir('hello world')

<!-- -->
    [
        ...
        'find',
        'format',
        'format_map',
        'index',
        'isalnum',
        ...
    ]

---
# Variables are pointers to objects

    !python
    x = [1, 2, 3]
    y = x
    z = [x, x]
    x = 33
    y.append(10)

    print(x)
    print(y)
    print(z)

<!-- -->
    33
    [1, 2, 3, 10]
    [[1, 2, 3, 10], [1, 2, 3, 10]]

---
# Exercise - Variables & Collections
* Create a list containing some integer values
* Create a second list which contains the first list twice
* Append a string to the first list
* Print the second list

---
# Functions
* Functions in Python can be standalone (do not need to be attached to a class)
* Defined using the `def` keyword
* Return values using the `return` keyword
* Arguments can be passed by name or position

---
# Functions

    !python
    def add(x, y, z):
        return x + y + z

    print(add(1, 2, 3))

    # x is passed implicitly; y & z are passed explicitly
    print(add(1, z=7, y=3))

<!-- -->
    6
    11

---
# Default arguments
* Default arguments can be defined on functions using the `=` syntax
* If the argument in that position is not defined, it will get the default

<!-- -->

    !python
    def print_greeting(username='anonymous'):
        print('Welcome, {}'.format(username))

    print_greeting('George')
    print_greeting()

<!-- -->
    'Welcome, George'
    'Welcome, anonymous'


---
# Classes
* Classes are defined using the `class` keyword
* The special method named `__init__` is the constructor
* All methods* take a first parameter, `self`, which references the particular object
* Python does not have private variables; the convention is that variables attached to the object with a underscore prefix are "considered" private

\* - The special cases of
[@classmethod](https://docs.python.org/3.6/library/functions.html#classmethod) &
[@staticmethod](https://docs.python.org/3.6/library/functions.html#staticmethod) do not take the `self` parameter. These methods are not covered in this course

---
# Classes

    !python
    class Dog:
        def __init__(self, name, age):
            self._name = name
            self._age = age

        def describe(self):
            print('My name is {} and my age is {}'.format(self._name, self._age))

    my_dog = Dog('Rover', 3)
    my_dog.describe()

<!-- -->
    
    My name is Rover and my age is 3

---
# Exercise - Calculator Class
* Create a class named Calculator
* It's `__init__` method takes two arguments
* Create methods on the Calculator class called:
    - `add`
    - `subtract`
    - `mult`
    - `divide`
* This methods should each return the result of the calculations
* Create an object of type Calculator and test each of the methods

---
# Class Inheritance
* Classes inherit using the syntax `Class(Subclass1, Subclass2):`
* Child classes have access to all methods and variables (nothing really private)
* Call the parent methods with `super()`

---
# Class Inheritance - Abstract Class
    !python
    class Animal:
        def __init__(self, name, age):
            self._name = name
            self._age = age

        def describe(self):
            return 'This is {} and she is {} years old.'.format(
                self._name, self._age)

        def speak(self):
            raise NotImplemented('speak method is not implemented')

---
# Class Inheritance - Child Class
    !python
    class Dog(Animal):
        def __init__(self, name, age, breed):
            super().__init__(name, age)
            self._breed = breed

        def speak(self):
            return 'Woof woof!'

        def describe(self):
            return super().describe() +
                ' She is a {}'.format(self._breed)

---
# Class Inheritance - Run

    !python
    my_dog = Dog('Daisy', 3, 'Labrador')

    description = my_dog.describe()
    print('Description: {}'.format(description))

    speech = my_dog.speak()
    print('She says: "{}"'.format(speech))

<!-- -->
    Description: This is Daisy and she is 3 years old. She is a Labrador
    She says: "Woof woof!"
