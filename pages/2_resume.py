import streamlit as st
import requests
from PIL import Image


#from IPython.display import HTML


def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")
pg_bg_gradient = """

<style>
body {
background-image: linear-gradient(to right top, #f4bedc, #e7b8df, #d7b2e3, #c3aee6, #acabe8, #979edb, #8192cd, #6c86bf, #596ea2, #465786, #33416b, #212c51);
}
</style>

"""
st.markdown(pg_bg_gradient, unsafe_allow_html=True)

st.title("Resume")
st.markdown("## Ripunjay Singh")
res1 = Image.open("images/res1.jpg")
res2 = Image.open("images/res2.jpg")
st.image(res1, use_column_width=True)
st.image(res2,use_column_width=True)

# PDF file URL
pdf_url = "https://github.com/rpj09/Portfolio/blob/master/images/rpjres.pdf?raw=true"

# Download button
if st.button("Download Resume"):
    response = requests.get(pdf_url)
    with open("rpjres.pdf", "wb") as f:
        f.write(response.content)
    st.success("Download complete!")