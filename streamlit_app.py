
import streamlit
import pandas




streamlit.title('my parents New Healthy Diner')
streamlit.header('Breakfact Menu')
streamlit.text('🥣Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗Kale,spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞Hard-Boiled Free Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
