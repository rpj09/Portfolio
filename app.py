
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

pg_bg_gradient = """

<style>
[class="main css-uf99v8 egzxvld5"]{
background-image: linear-gradient(to right top, #f4bedc, #e7b8df, #d7b2e3, #c3aee6, #acabe8, #979edb, #8192cd, #6c86bf, #596ea2, #465786, #33416b, #212c51);
}
</style>

"""

#background-image: linear-gradient(to right top, #f4bedc, #e7b8df, #d7b2e3, #c3aee6, #acabe8, #979edb, #8192cd, #6c86bf, #596ea2, #465786, #33416b, #212c51);
#background-image: radial-gradient(circle, rgba(211,170,245,0.966999299719888) 0%, rgba(15,2,37,0.9810049019607843) 95%);
# [class="css-1kyxreq etr89bj2"] img {
#   width: 100%;
#   height: 100%;
#   transition: transform 0.75s ease-in-out;
#   transform-style: preserve-3d;
# }
# [class="css-1kyxreq etr89bj2"]:hover img {
#   transform: rotateY(180deg);
# }

#st-bv st-bw st-b6 st-b5 st-ar st-as st-bx st-by st-bz st-c0 st-c1 st-c2 st-c3 st-c4 st-c5 st-c6 st-c7 st-c8 st-c9 st-ca st-cb st-cu st-cd st-ce st-b1 st-cf st-cg st-ch st-ci st-cj st-ck st-cl st-cm st-ae st-cn st-ag st-ah st-ai st-aj st-co st-cp st-cq st-cr st-cs st-ct
#st-bv st-bw st-b6 st-b5 st-ar st-as st-bx st-by st-bz st-c0 st-c1 st-c2 st-c3 st-c4 st-c5 st-c6 st-c7 st-c8 st-c9 st-ca st-cb st-cu st-cd st-ce st-b1 st-cf st-cg st-ch st-ci st-cj st-ck st-cl st-cm st-ae st-cn st-ag st-ah st-ai st-aj st-co st-cp st-cq st-cr st-cs st-ct


#after flip card another image
card = """
<style>
[class="css-1kyxreq etr89bj2"]{
    justify-content: center;
}
</style>
"""

tansbuttonbg1 = """
<style>
[class="st-c7"]{
background: transparent;
}
</style>
"""
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
#background-image: linear-gradient(180deg, rgba(11,16,19,1) 0%, rgba(4,34,54,1) 50%, rgba(9,16,21,1) 100%);

#background-image: linear-gradient(to right top, #f4bedc, #e7b8df, #d7b2e3, #c3aee6, #acabe8, #979edb, #8192cd, #6c86bf, #596ea2, #465786, #33416b, #212c51);

#setting configurations
st.set_page_config(page_title="Ripunjay Singh Portfolio",layout="wide",initial_sidebar_state="expanded")
st.markdown(pg_bg_gradient, unsafe_allow_html=True)
st.markdown(card, unsafe_allow_html=True)
st.markdown(tansbuttonbg1, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




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
git_lottie = load_lottie("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
Andorid_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_fztluxdp.json")
Docker_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
Linux_lottie = load_lottie("https://assets2.lottiefiles.com/packages/lf20_drcnxdtp.json")
Xcode_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
firebase_lottie = load_lottie("https://assets5.lottiefiles.com/private_files/lf30_52jsgl4a.json")
img_proj1 = Image.open("images/FRIDAY.png")
img_proj2 = Image.open("images/1.png")
gireverb = Image.open("images/gitreverb.png")
github_card = Image.open("images/gitcardmain.png")

Home,Resume = st.tabs(["Home","Resume"])


with Home:
    with st.container():
        left_column,right_column = st.columns(2)
        with left_column:
            st.subheader("Hi, I am Ripunjay :wave:")
            st.title("A passionate learner and Python Developer")
            st.write("I am passionate about learning different technologies and finding ways to automate stuff using python")

            st.write("[Explore more about my work on github ](https://github.com/rpj09)")

    with right_column:
        st_lottie(lottie_gif, height=400, key="coding")

    with st.container():
        column_widths = [2, 1]
        left_column,right_column = st.columns(column_widths)
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
            st.subheader("Github Contribution Graph")
            st.image("https://ghchart.rshah.org/9442e3/rpj09",use_column_width=True)
        with right_column:

            st.image(github_card,use_column_width=True)      


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
            st.image(gireverb, width=200)

        with text_column:

            st.subheader("GitReverb")
            st.write("""
            A Social Media webapp for developers to share their projects and get feedback from other developers.
            A web app to visualize your github profile and repositories.
            """)
            

            st.markdown("[Checkout the project source code here...](https://github.com/rpj09/GitReverb)")

    with st.container():

        st.header("My Skills :")
        st.subheader("Languages:")
        with st.container():
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
                #st.image(Image.open('python_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Python")
            with col2:
                st_lottie(java_lottie, height=70,width=70, key="java", speed=4)
                #st.image(Image.open('java_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Java")
            with col3:
                st_lottie(swift_lottie,height=70,width=70, key="swift", speed=2.5)
                #st.image(Image.open('javascript_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Swift")
            with col1:
                st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
                #st.image(Image.open('sql_logo.png').resize((100,100)), use_column_width=True)
                #st.write("MYSQL")
            with col2:
                st_lottie(firebase_lottie, height=70,width=70, key="Firebase", speed=4)



        st.subheader("Frameworks:")
        with st.container():
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.image("https://www.vectorlogo.zone/logos/djangoproject/djangoproject-ar21.svg",width=70)
                #st.image(Image.open('flask_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Flask")
            with col2:
                st.image("https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.svg",width=70)
                #st.image(Image.open('django_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Django")

        st.subheader("Tools:")
        with st.container():
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st_lottie(git_lottie,height=70,width=70, key="Git", speed=2.5)
                #st.image(Image.open('git_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Git")
            with col1:
                st_lottie(github_lottie,height=70,width=70, key="Github", speed=2.5)
                #st.image(Image.open('git_logo.png').resize((100,100)), use_column_width=True)
                #st.write("GitHub")
            with col2:
                st_lottie(Andorid_lottie,height=70,width=70, key="Android Studio", speed=2.5)
                #st.image(Image.open('jupyter_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Android Studio")
            with col3:
                st.image("https://www.vectorlogo.zone/logos/visualstudio_code/visualstudio_code-icon.svg",width=80)
                #st.image(Image.open('vscode_logo.png').resize((100,100)), use_column_width=True)
                #st.write("VS Code")
            with col1:
                st_lottie(Linux_lottie,height=70,width=70, key="Linux", speed=2.5)
                #st.image(Image.open('pycharm_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Linux")
            with col2:
                st_lottie(Docker_lottie,height=100,width=100, key="docker", speed=2.5)
                #st.image(Image.open('pycharm_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Docker")
            with col3:
                st.image("https://www.vectorlogo.zone/logos/apple_xcode/apple_xcode-ar21.svg",width=160)
                #st.image(Image.open('mysql_logo.png').resize((100,100)), use_column_width=True)
                #st.write("Xcode")


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

with Resume:
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


