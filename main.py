import streamlit as st

# This is a Chainlit application that wishes Azlaan a happy birthday in both English and Urdu.
st.title("🎂HAPPY BIRTDAY AZALAN ❤")
st.write("I created this app for You on your special DAY ")

number_input = st.number_input("Enter a number:", value=0)


# ✅ Your original functions or classes here
def greet(name):
    return f"Wllcom to my cute Nephew AZALAAN, {name} HAPPY BIRTHDAY TO YOU."

def multiply_by_two(n):
    return n * 2

# 🎯 Button to trigger your logic
if st.button("Run Logic"):
    # Call your functions using the inputs
    greeting = greet(number_input)

    doubled = multiply_by_two(number_input)

    # Show results
    st.success(greeting)
    st.info(f"{number_input} multiplied by 2 is {doubled}.")

# ✅ You can also add more logic or display anything you like
# st.write("---")
# st.write("Tip: Edit this file to add more functionality as needed.")