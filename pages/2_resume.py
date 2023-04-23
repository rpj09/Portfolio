import streamlit as st
import requests

#from IPython.display import HTML


def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

st.title("Resume")

st.text('coming soon...')

# Display PDF at the bottom
pdf_url = "https://raw.githubusercontent.com/rpj09/Portfolio/master/images/rpjres.pdf"
response = requests.get(pdf_url)
#pdf_height = 1000
with open("dummy.pdf", "wb") as f:
    f.write(response.content)

with open("dummy.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
st.write(pdf_display, unsafe_allow_html=True)
#st.embed_pdf(pdf_url, width=700, height=900)
#st.markdown(f'<iframe src="{pdf_url}" width="100%" height="{pdf_height}px"></iframe>', unsafe_allow_html=True)