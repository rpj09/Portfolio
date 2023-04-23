import streamlit as st
import io
import base64
import fitz

def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

st.title("Resume")

st.text('coming soon...')

# Display PDF at the bottom
pdf_url = "https://raw.githubusercontent.com/rpj09/Portfolio/master/images/rpjres.pdf"
pdf_height = 800

with fitz.open(pdf_url) as doc:
    pdf_bytes = doc.get_pdf()
    
b64 = base64.b64encode(pdf_bytes)
st.markdown(f'<embed src="data:application/pdf;base64,{b64.decode()}" width="100%" height="{pdf_height}" type="application/pdf">', unsafe_allow_html=True)
