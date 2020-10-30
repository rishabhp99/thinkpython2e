# A function object is a value you can assign to a variable or pass as an argument. For
# example, do_twice is a function that takes a function object as an argument and calls it twice:
# def do_twice(f):
# f()
# f()
# Here’s an example that uses do_twice to call a function named print_spam twice.
# def print_spam():
# print('spam')
# do_twice(print_spam)
# 1. Type this example into a script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
# function twice, passing the value as an argument.
# 3. Copy the definition of print_twice from earlier in this chapter to your script.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
# argument.
# 5. Define a new function called do_four that takes a function object and a value and calls the
# function four times, passing the value as a parameter. There should be only two statements in
# the body of this function, not four

# 1.

def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')


do_twice(print_spam)

# 2.


def do_twice(f, val):
    f(val)
    f(val)


def print_value(val):
    print(val)


do_twice(print_value, "42")
