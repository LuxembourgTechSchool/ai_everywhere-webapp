import streamlit as st

# Initialize session state variables if they don't exist
if 'quiz_position' not in st.session_state:
    st.session_state['quiz_position'] = False

if 'quiz_condition' not in st.session_state:
    st.session_state['quiz_condition'] = False

if 'quiz_var' not in st.session_state:
    st.session_state['quiz_var'] = False

if 'quiz_apple' not in st.session_state:
    st.session_state['quiz_apple'] = False

if 'quiz_condition2' not in st.session_state:
    st.session_state['quiz_condition2'] = False

if 'quiz_for' not in st.session_state:
    st.session_state['quiz_for'] = False

st.title("Learn Python Basics with Streamlit")

#------------------------------------------------------------
# Variables
st.header("1. Variables")
st.write("Variables are like containers that hold information. For example:")
x = 10
st.code("x = 10", language='python')
st.write(f"x is an integer and the value of x is {x}")
lts = "Luxembourg Tech School"
st.code('lts = "Luxembourg Tech School"', language='python')
st.write(f"lts is a string and the value of lts is {lts}")

st.write("Let's create a new variable called year that stores the year Python was first released.")
guessed_var = st.text_input("Enter the variable", key='var')
guessed_var = guessed_var.replace(" ", "")

if st.button("Check", key='check_button_var'):
    if guessed_var == "year=1991":
        st.success(f"Correct! The correct variable declaration and initialization is: {guessed_var}.")
        st.session_state['quiz_var'] = True
    else:
        st.error(f"Sorry, {guessed_var} is not the correct variable. Try again!")

#------------------------------------------------------------
# Lists
st.header("2. Lists")
st.write("Lists [] are like a collection of items. For example:")
my_list = ['apple', 'banana', 'cherry']
st.code("my_list = ['apple', 'banana', 'cherry']", language='python')
st.write(f"The list contains: {my_list}")

st.write("What is the position of cherry?")
guessed_position = st.text_input("Enter the position", key='position')

if st.button("Check", key='check_button_1'):
    if guessed_position.isdigit() and int(guessed_position) == 2:
        st.success(f"Correct! cherry is at position {guessed_position}.")
        st.session_state['quiz_position'] = True
    else:
        st.error(f"Sorry, cherry is not at position {guessed_position}. Try again! Hint: computers start counting at 0.")

st.write("How can we get not the entire list but only the apple? Hint: we need to access the correct position.")
guessed_apple = st.text_input("Enter the code to get the apple", key='apple')
guessed_apple = guessed_apple.replace(" ", "")

if st.button("Check", key='check_button_apple'):
    if guessed_apple == "my_list[0]" or guessed_apple == "print(my_list[0])":
        st.success(f"Correct! To get only the apple we need {guessed_apple}.")
        st.session_state['quiz_apple'] = True
    else:
        st.error(f"Sorry, {guessed_apple} does not return the apple. Try again! Hint: you can use [...] on the list to access a specific position")

st.write("To get the length (amount of elements) of a list [], we can use the len() function. For example:")
my_list = ['apple', 'banana', 'cherry']
st.code("""
my_list = ['apple', 'banana', 'cherry']
print(len(my_list))
""", language='python')
st.write(f"The length of the list is: 3")

#------------------------------------------------------------
# If Statements
st.header("3. If Statements")
st.write("If statements help us make decisions based on conditions. For example:")
st.code("""
x = 10
if x > 5:
    st.write('x is greater than 5')
else:
    st.write('x is not greater than 5')
""", language='python')
if x > 5:
    st.write('x is greater than 5')
else:
    st.write('x is not greater than 5')


st.write("Consider this code: ")
st.code("""
if condition:
    st.write('You are an adult')
else:
    st.write('You are still a teenager')
""", language='python')
st.write("There exists a variable called age. Enter the required condition to get the correct output.")

guessed_condition = st.text_input("Enter the condition", key='condition')

if st.button("Check", key='check_button_condition'):
    stripped_condition = guessed_condition.replace(" ", "")
    if stripped_condition == "age>=18":
        st.success(f"Correct! {guessed_condition} is the correct condition.")
        st.code(f"""
if {guessed_condition}:
    st.write('You are an adult')
else:
    st.write('You are still a teenager')
""", language='python')
        st.session_state['quiz_condition'] = True
    else:
        st.error(f"Sorry, {guessed_condition} is not the correct condition. Try again!")


st.write("Variables can not only be integers (numbers) and strings (text) but they cal also be boolean.")
st.write("Those variables hold the information True or False. For example:")
python_is_fun = True
st.code("python_is_fun = True", language='python')
st.write(f"python_is_fun is a boolean and the value of python_is_fun is {python_is_fun}.")

st.write("With an if statement we can also check multiple conditions and only do a specific action if e.g. at least one of the conditions is true. \nFor example:")
st.code("""
if degrees < 5 or sun == False:
    st.write('The weather is bad')
else:
    st.write('The weather is good')
""", language='python')


st.write("Consider this code: ")
st.code("""
if conditions:
    st.write('You are an adult and you are allowed to drive')
else:
    st.write('You are not allowed to drive')
""", language='python')
st.write("There exists an integer variable called 'age' and a boolean variable 'license'. Enter the required condition to get the correct output.")

guessed_condition = st.text_input("Enter the condition", key='condition2')

if st.button("Check", key='check_button_condition2'):
    stripped_condition = guessed_condition.replace(" ", "")
    if stripped_condition == "age>=18andlicense==True":
        st.success(f"Correct! {guessed_condition} is the correct condition.")
        st.code(f"""
if {guessed_condition}:
    st.write('You are an adult and you are allowed to drive')
else:
    st.write('You are not allowed to drive')
""", language='python')
        st.session_state['quiz_condition2'] = True
    else:
        st.error(f"Sorry, {guessed_condition} is not the correct condition. Try again! Hint: you need to combine 2 conditions and you can compare values using ==")

#------------------------------------------------------------
# For Loops
st.header("4. For Loops")
st.write("For loops allow us to repeat actions for each item in a list. For example:")
st.code("""
for fruit in my_list:
    st.write(fruit)
""", language='python')

for fruit in my_list:
    st.write(fruit)

st.write("For loops also allow us to repeat actions a given number of times. For example:")
st.code("""
for i in range(5):
    print(i)
    print("Hello")
""", language='python')

st.write("This gives:  \n0 Hello  \n1 Hello  \n2 Hello  \n3 Hello  \n4 Hello")

st.write("Consider this code where we want to calculate the sum of all the numbers in a list: ")
st.code("""
my_numbers = [1,2,3,4,5,6]
sum = 0
ForLoop
    CalculateSum
print(sum)
""", language='python')


st.write("Write the missing code for the for loop and sum calculation. Use 'n' as variable name in the for loop.")

guessed_for = st.text_input("Enter the for loop:", key='for')
guessed_sum = st.text_input("Enter the code to calculate the sum:", key='sum')

if st.button("Check", key='check_button_for'):
    guessed_for2 = guessed_for.replace(" ", "")
    guessed_sum2 = guessed_sum.replace(" ", "")
    #st.write(guessed_for2)
    #st.write(guessed_sum2)
    if guessed_for2 == "forninrange(len(my_numbers)):" and (guessed_sum2 == "sum=sum+my_numbers[n]" or guessed_sum2 == "sum+=my_numbers[n]"):
        st.success(f"Correct! {guessed_for} is the correct for loop and {guessed_sum} is the correct way to calculate the sum.")
        st.code(f"""
if {guessed_for}:
my_numbers = [1,2,3,4,5,6]
sum = 0
{guessed_for}
    {guessed_sum}
print(sum)
""", language='python')
        st.session_state['quiz_for'] = True
    elif guessed_for2 == "forninmy_numbers:" and (guessed_sum2 == "sum=sum+n" or guessed_sum2 == "sum+=n"):
        st.success(f"Correct! {guessed_for} is the correct for loop and {guessed_sum} is the correct way to calculate the sum.")
        st.code(f"""
if {guessed_for}:
my_numbers = [1,2,3,4,5,6]
sum = 0
{guessed_for}
    {guessed_sum}
print(sum)
""", language='python')
        st.session_state['quiz_for'] = True
    else:
        st.error(f"Sorry, this is not correct. Try again! Hint: you can use range, len and the position of every item.")


# Check if all quizzes are completed and show balloons
if st.session_state['quiz_position'] and st.session_state['quiz_condition']  and st.session_state['quiz_var'] and st.session_state['quiz_apple'] and st.session_state['quiz_condition2'] and st.session_state['quiz_for']:
    st.balloons()
