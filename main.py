#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name is not a valid name in Python because variable names cannot start with a number.
3. age is a valid name in Python because it only contains lowercase letters with no spaces or special characters.
4. total_amount is a valid name in Python because it follows snake case and uses only allowed characters.
5. while is not a valid name in Python because it is a reserved keyword used to define loops.
6. Student is a valid name in Python, but capitalized names are usually used for classes, not variables.
7. my-variable is not a valid name in Python because hyphens are not allowed in variable names.
8. for is not a valid name in Python because it is a reserved keyword used in loops.
9. _temp is a valid name in Python because variable names can begin with an underscore.
10. value# is not a valid name in Python because special characters like '#' are not allowed in variable names.
"""


"""
# Problem 2
1. calculate_total is a valid function name in Python because it uses snake case and only contains allowed characters.
2. 3rd_function is not a valid function name in Python because function names cannot start with a number.
3. print_values is a valid function name in Python because it follows snake case and uses only lowercase letters and underscores.
4. find-item is not a valid function name in Python because hyphens are not allowed. Python takes - as a subtraction operator.
5. def is not a valid function name in Python because it is a reserved keyword.
6. updateProfile is a valid function name in Python, but it uses camel case instead of snake case.
7. my_function is a valid function name in Python because it uses snake case and only includes valid characters.
8. try is not a valid function name in Python because it is a reserved keyword.
9. init_data is a valid function name in Python because it follows snake case and uses only letters and underscores.
10. value@function is not a valid function name in Python because special characters like @ are not allowed in function names.
"""


"""
# Problem 3
1. True and False results in False because both values are boolean, and 'and' returns True only if both are True.
2. 5 > 3 or "apple" < "banana" is True because 5 > 3 is True, and 'or' returns True if at least one condition is True.
3. not 10 <= 20 is False because 10 <= 20 is True, and 'not' makes it False.
4. True or 5 = 4 is not valid because '=' is an assignment operator, It should use '==' instead.
5. "apple" != "orange" and 5 results to 5 because "apple" != "orange" is True, and 'and' gives the second value if both parts are True.
6. 3 < 5 not True is not valid because there is no operator between 5 and not. It needs to be written more clearly or with parentheses.
7. False == (3 > 4) is to True because 3 > 4 is False, and False == False is True.
8. 10 <= "10" is not valid because Python cannot compare an integer and a string.
9. True or not False is True because not False is True.
10. 5 and or 4 is not valid because 'and' and 'or' need valid expressions on both sides.
"""

#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict)
list_keys = list(some_dict.keys())
    list_values = list(some_dict.values())
    return list_keys, list_values
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
if string_operator == "and":
        return boolean1 and boolean2
    elif string_operator == "or":
        return boolean1 or boolean2
    elif string_operator == "not":
        return not boolean1 or not boolean2
    else:
        return False
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
a_list is just one example of a the kind of input you could recieve
a_list = [3,4,5,6,7]
odd_list = [3,5,7]
    """
    odd_list = []
    for number in a_list:
        if number % 2 != 0:
            odd_list.append(number)
    return odd_list
    
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
if len(numbers_list) == 0:
        return 0
    total = sum(numbers_list)
    average = total / len(numbers_list)
    return average
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
