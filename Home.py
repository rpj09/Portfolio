
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


#setting configurations
st.set_page_config(page_title="My Portfolio",page_icon=":point_down:", layout="wide")


def load_lottie(link):
    r = requests.get(link)
    if r.status_code !=200:
        return  None
    return None if r.status_code != 200 else r.json()


def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

#loading assets

lottie_gif = load_lottie("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_proj1 = Image.open("images/FRIDAY.png")
img_proj2 = Image.open("images/1.png")


with st.container():
    st.subheader("Hi, I am Ripunjay :wave:")
    st.title("A passionate learner and Python Developer")
    st.write("I am passionate about learning different technologies and finding ways to automate stuff using python")
    st.write("[Explore more about my work>](https://github.com/rpj09)")

    left_column,right_column = st.columns(2)
    with left_column:
        st.write("---")
        st.header("What do I do")
        st.write('##')
        st.write(
            """
            Currently I am Student who just cleared High School
            
            - Started My coding Journey Last year and Explored Python and automation stuff
            
            - Newly Learned Bash scripting and now on my way to explore it further

            - and I have my current skillset in Python,Mysql,linux and Bash scripting

            - ...
            
            """
        )
with right_column:
    st_lottie(lottie_gif, height=300, key="coding")



with st.container():
    st.write("---")
    st.header("My Projects")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_proj1)

    with text_column:
        st.subheader("Wanna make your life easier , I've got something for you")
        st.write(
            """
            Automate your linux/Windows System just at your voice!
            From sending whatsapp messages to downloading youtube video you are looking at , with just a voice command

            ~and for developers who want to contribute there is always a place
            """
        )
        st.markdown("[Checkout the project source code here...](https://github.com/rpj09/FRIDAY-virtual-assistant)")

with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_proj2)

    with text_column:

        st.subheader("My personal portfolio website")

        st.markdown("[Checkout the project source code here...](https://github.com/rpj09/Portfolio_website_using_python)")







with st.container():
    st.write("---")
    st.header("Get in Touch With Me!")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/singhripunjay09+portfolio@gmail.com" method="POST">
        <input type="hidden" name="_captcha value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column,right_column = st.columns(2)

    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty() 
