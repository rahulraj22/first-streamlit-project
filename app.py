from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# lets set some basic page configurations...
st.set_page_config(page_title = 'My Webpage', page_icon = ':tada:', layout = 'wide')  # for emoji: https://www.webfx.com/tools/emoji-cheat-sheet/

# This function will try to access json data of the lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  # Here we are returning the json data of the lottie animation.


# ------ Use Local CSS --------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("./style/style.css")  # calling function local_css(argument as location of that file)



# ------ LOAD ASSETS ----------
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_contact_form = Image.open('./images/contactForm.jpg')
image_lottie_animation = Image.open('./images/animation.jpg')



# Lets set the header section:--
with st.container():
    st.subheader("Hi, I am Rahul :wave:")
    st.title("A Data Analyst from India")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings.")
    st.write("[Learn more>](https://rahulraj22.github.io/cv)")

# What I do in detail:------
with st.container():
    st.write("---") # here we use a divider(similar to hr in html)
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What I do')
        st.write('##') # this will give give space/margin below the header content
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks for Blog writing and are looking for a way to use Python.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."
            
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[My CV>](https://rahulraj22.github.io/cv/)")
    
    with right_column:
        # this is the right_column where we will insert the animation:
        st_lottie(lottie_coding, height = 300, key = 'coding')
        
        
#-----  Projects Sections ------------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    
    # lets insert the image:
    with image_column:
        st.image(image_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit! 
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it! 
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/@rahulrajsjs22)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website? 
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/SSlZ2OD61Qw)")
        
# --------- CONTACT FORM -----------
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    # Documentations: https://formsubmit.co/  : form section inside """..."""
    contact_form = """
    <form action="https://formsubmit.co/rahulrajsjs22@gmail.com" method="POST">
        <input type = "hidden" name = "_captcha" value = "false">
        <input type="text" name="name" placeholder = "Your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name = "massage" placeholder = "Your massage here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html = True)
    with right_column:
        st.empty()


# install package: pip install pipreqs
# this will name all the packages required for your app(while deploying online)
# after this type command: pipreqs --encoding=utf8 (enter)
# (Above command will automatically create new file named requirements.txt => displays the lists of all libraries required for my app)