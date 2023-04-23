import streamlit as st

def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

st.title("Resume")

st.text('coming soon....')



# Display PDF at the bottom
pdf_url = "https://github.com/rpj09/Portfolio/blob/master/images/Resume-Ripunjay-Singh%2Bnew.pdf?raw=true"
pdf_height = 800
st.markdown(f'<iframe src="{pdf_url}" width="100%" height="{pdf_height}" frameborder="0"></iframe>', unsafe_allow_html=True)