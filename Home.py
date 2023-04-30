
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
python_lottie = load_lottie("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottie("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
swift_lottie = load_lottie("https://assets3.lottiefiles.com/packages/lf20_inopzfvq.json")
my_sql_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
img_proj1 = Image.open("images/FRIDAY.png")
img_proj2 = Image.open("images/1.png")
gireverb = Image.open("images/gitreverb.png")



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
            Currently I am In my 1st year of B.Tech in Computer Science and Engineering
            
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
        st.subheader("FRIDAY")
        st.write("Wanna make your life easier , I've got something for you")
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
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(gireverb)

    with text_column:

        st.subheader("GitReverb")
        st.write("""
        A Social Media webapp for developers to share their projects and get feedback from other developers.
        A web app to visualize your github profile and repositories.
        """)
        

        st.markdown("[Checkout the project source code here...](https://github.com/rpj09/GitReverb)")

with st.container():

    st.header("I have my skill set in:")
    st.subheader("Languages")
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st_lottie(python_lottie, height=100, key="python", speed=2.5)
            #st.image(Image.open('python_logo.png').resize((100,100)), use_column_width=True)
            st.write("Python")
        with col2:
            st_lottie(java_lottie, height=50,width=50, key="java", speed=2.5)
            #st.image(Image.open('java_logo.png').resize((100,100)), use_column_width=True)
            st.write("Java")
        with col3:
            st_lottie(swift_lottie, height=100, key="swift", speed=2.5)
            #st.image(Image.open('javascript_logo.png').resize((100,100)), use_column_width=True)
            st.write("Swift")
        with col1:
            #st.image(Image.open('sql_logo.png').resize((100,100)), use_column_width=True)
            st.write("SQL")
        with col2:
            #st.image(Image.open('html_css_logo.png').resize((100,100)), use_column_width=True)
            st.write("HTML/CSS")

        st.markdown(
            """
            <style>
            .column {text-align: center;}
            </style>
            """,
            unsafe_allow_html=True
        )
        for col in [col1, col2, col3]:
            col.markdown("<div class='column'></div>", unsafe_allow_html=True)
    st.subheader("Frameworks")
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            #st.image(Image.open('flask_logo.png').resize((100,100)), use_column_width=True)
            st.write("Flask")
        with col2:
            #st.image(Image.open('django_logo.png').resize((100,100)), use_column_width=True)
            st.write("Django")
        with col3:
            #st.image(Image.open('react_logo.png').resize((100,100)), use_column_width=True)
            st.write("React")
        with col1:
            #st.image(Image.open('angular_logo.png').resize((100,100)), use_column_width=True)
            st.write("Angular")
        with col2:
            #st.image(Image.open('nodejs_logo.png').resize((100,100)), use_column_width=True)
            st.write("Node.js")
    st.subheader("Tools")
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            #st.image(Image.open('git_logo.png').resize((100,100)), use_column_width=True)
            st.write("Git")
        with col2:
            #st.image(Image.open('jupyter_logo.png').resize((100,100)), use_column_width=True)
            st.write("Jupyter Notebook")
        with col3:
            #st.image(Image.open('vscode_logo.png').resize((100,100)), use_column_width=True)
            st.write("VS Code")
        with col1:
            #st.image(Image.open('pycharm_logo.png').resize((100,100)), use_column_width=True)
            st.write("PyCharm")
        with col2:
            #st.image(Image.open('mysql_logo.png').resize((100,100)), use_column_width=True)
            st.write("MySQL Workbench")


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
