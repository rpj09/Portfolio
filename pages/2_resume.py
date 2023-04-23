import streamlit as st
impot requests
from PIL import Image


#from IPython.display import HTML


def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

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