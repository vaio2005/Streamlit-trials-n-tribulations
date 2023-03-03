import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Lists",
    page_icon=":receipt:",
    layout="wide",
)

st.title("Lists")

st.header("What is a list?")
st.write("A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don’t have to be related in any particular way. Because a list usually contains more than one element, it is a good idea to make the name of your list plural, such as letters, digits, or names. In Python, square brackets (`[]`) indicate a list, and individual elements in the list are separated by commas.")

st.header("How do I make a list?")
st.write("To make a list, put square brackets around the items you want to store in the list. You can make an empty list that contains no items by using empty square brackets, like this: `numbers = []`")

st.header("How do I access items in a list?")
st.write("You access items in a list by telling Python the position, or index, of the item desired. To access an item in a list, write the name of the list followed by the index of the item enclosed in square brackets. Remember that Python counts from zero, so the first item in a list will be at index 0.")

st.header("How do I change an item in a list?")
st.write("To change an item in a list, use the name of the list followed by the index of the item you want to change, and then provide the new value you want that item to have.")

st.header("How do I add items to a list?")
st.write("You can add items to the end of a list using the `append()` method. You can also add items at any position in your list by using the `insert()` method.")

st.header("How do I remove items from a list?")
st.write("You can remove an item from a list using the `del` statement if you know its position in the list. You can also use the `pop()` method to remove an item from a list, and then work with that item after removing it.")

st.header("How do I sort a list?")
st.write("You can sort a list permanently with the `sort()` method. The `sort()` method changes the order of a list permanently. The `sorted()` function lets you display your list in a particular order but doesn’t affect the actual order of the list.")

st.header("How do I find the length of a list?")
st.write("To find out how many items are in a list, use the `len()` function.")

st.header("How do I loop through a list?")
st.write("You can loop through the elements in a list using a for loop. All you have to do is specify the name of the list you want to work with, and the name of a temporary variable that will hold each item in turn as the loop processes the list. Python will pull the first item from the list and store it in the temporary variable, then run the code inside the loop once, using the current item to replace the temporary variable. Python will then pull the next item from the list and store it in the temporary variable, and it will continue until it runs out of items.")

st.header("How do I make a list of numbers?")
st.write("You can use the `range()` function to quickly generate a large number of numbers.")

st.header("Enoguh talk, let's try it out!")

st.write("Let's make a list of the first 10 square numbers.")
st.write("First, we need to make an empty list. We can do this by using square brackets, like this: []")
st.code("squares = []", language="python")

squares = []
for value in range(0,11):
    square = value**2
    squares.append(square)

st.write("Now, let's use a for loop to add the first 10 square numbers to the list.")
st.code("""
for value in range(0,11):
    square = value**2
    squares.append(square)
""", language="python")

st.write("In Streamlit, we can display lists easily using the st.write() function, but we can also use the st.dataframe() function to display lists in a table.")
st.write("Let's display the list of squares in a table.")
st.code("""st.dataframe(pd.DataFrame(squares, columns=["Square"]))""", language="python")

st.write("And this is what it will look like:")
st.dataframe(pd.DataFrame(squares, columns=["Square"]))

st.write("That was easy, and kind of boring... Let's try something a little more interesting.")
st.write("Let's make a list of your favourite superheros!")
st.write("First, we need to make an empty list. I'm sure you remember how")
st.write("Second, let's use a for loop to add your favourite superheros to the list, using the st.text_input() function to get the input from you.")
st.write("Finally, let's display the list of superheros in a table.")

st.code("""
superheros = []
for i in range(0,3):
    superheros.append(st.text_input("What is your favourite superhero?", key=i))
st.dataframe(pd.DataFrame(superheros, columns=["Superhero"]))
""", language="python")

st.write("And this is what it will look like:")

superheros = []
for i in range(0,3):
    superheros.append(st.text_input("What is your favourite superhero?", key=i))
st.dataframe(pd.DataFrame(superheros, columns=["Superhero"]))

st.write("That's it for lists! Let's move on to the next topic.")