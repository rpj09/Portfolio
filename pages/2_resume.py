import streamlit as st

def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

st.title("Resume")

st.text('coming soon...')

# Display PDF at the bottom
pdf_url = "https://raw.githubusercontent.com/rpj09/Portfolio/master/images/rpjres.pdf"


st.pdf_viewer(pdf_url)
