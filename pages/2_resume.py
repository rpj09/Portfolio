import streamlit as st


def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

st.title("Resume")

st.text('coming soon...')

# Display PDF at the bottom
pdf_url = "https://raw.githubusercontent.com/rpj09/Portfolio/master/images/rpjres.pdf"
pdf_height = 1000
st.markdown(f'<iframe src="{pdf_url}" width="100%" height="{pdf_height}px"></iframe>', unsafe_allow_html=True)