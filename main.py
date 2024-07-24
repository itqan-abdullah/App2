import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv",sep=";")
#print(df)
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.JPG")

with col2:
    st.title("Itqan Abdullah")
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore magna
    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
    ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate
    velit esse cillum dolore eu fugiat nulla pariatur.
    Officia deserunt mollit anim id est laborum.
    """
    st.info(content)

content2 = "Below are some of the apps I've made. Feel free to contact me."
st.write(content2)

col3,empty_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+ row['image'])
        st.write("[Source Code](https://github.com/itqan-abdullah)")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+ row['image'])
        st.write("[Source Code](https://github.com/itqan-abdullah)")
