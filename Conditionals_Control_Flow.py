#Comparators
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

#Boolean Operators
#This and That (or This, But Not That!)
bool_one = False or not True and True
bool_two = False and not True or True
bool_three = True and not (False or False)
bool_four = not not True or False and not True
bool_five = False or not (True and True)

#If, Else and Elif
def using_control_once():
    if 10 > 3:
        return "Success #1"

def using_control_again():
    if True or False:
        return "Success #2"

print (using_control_once())
print (using_control_again())

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if 5 > 4:    # Start coding here!
        return True # Don't forget to indent
                    # the code inside this block!
    elif 4 > 2 and -1 < 5:
        return True # Keep going here.
                    # You'll want to add the else statement, too!
    else:
        return True
