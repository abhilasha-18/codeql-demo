# app.py
def unsafe_input():
    user_input = input("Enter something: ")
    eval(user_input)  # Security issue (code injection)

unsafe_input()
