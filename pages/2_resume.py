import streamlit as st
import fitz

def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

st.title("Resume")

st.text('coming soon....')


st.text('Here is my Resume')

pdf_url = "https://raw.githubusercontent.com/rpj09/Portfolio/master/images/rpjres.pdf"
pdf_height = 800

with fitz.open(pdf_url) as doc:
    pdf_data = doc.convert_to_html()
st.markdown(pdf_data, unsafe_allow_html=True)
# Display PDF at the bottom
# pdf_url = "https://raw.githubusercontent.com/rpj09/Portfolio/master/images/rpjres.pdf"
# pdf_height = 800
# embed_pdf(pdf_url, height=pdf_height)

#st.markdown(f'<iframe src="{pdf_url}" width="100%" height="{pdf_height}" frameborder="0"></iframe>', unsafe_allow_html=True)