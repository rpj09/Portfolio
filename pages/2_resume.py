import streamlit as st
from PIL import Image


#from IPython.display import HTML


def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

st.title("Resume")

st.text('coming soon...')

st.text('here is my resume')

res1 = Image.open("res1.jpg")
res2 = Image.open("res2.jpg")
st.image(res1, use_column_width=True)
st.image(res2,use_column_width=True)