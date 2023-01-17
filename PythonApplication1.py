## Website 
import json
import requests
import streamlit as st
from PIL import Image
# from streamlit_lottie import st_lottie


st.set_page_config(page_title="Usayd's Webpage", page_icon=":tada:", layout="wide")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# load assets
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_dT1E1P.json")
lottie_program = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_es4p9zph.json")
lottie_boat = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fBnHxig6NO.json")
lottie_space = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_4tg3fb79.json")

# Header
with st.container():
    st.subheader("Welcome to my personal website :wave:")
    st.title("A future computer engineer studying at TMU")
    st.write("I have designed this website to demostrate my capabilities and understanding of code")
    st.write("[My Resume >](https://docs.google.com/document/d/1aCyPp37RvslOjPnqDrfpfWAEkk-zpR3_SL7CUCXzRaI/edit)")

# What I Do
with st.container():
    st.write("- - -")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Academic Background")
        st.write("##")
        st.write(
            """
            I am a first year computer engineering student enrolled at Toronto Metropolitan University
            - Current GPA: 2.93 (Semester 1)
            - Studying both software and hardware systems
            - Significant courses include: Programming Fundamentals, Electric Circuit Analysis, Engineering Economics

            """
            )
        with right_column:
            st_lottie(lottie_coding, height=300)

# Skills and Achievements
with st.container():
    st.write("- - - ")
    left_column, right_column = st.columns(2)
    with right_column:
        st.title("Skills and Achievements")
        st.write("##")
        st.write(
            """
            - Intermediate experience with C, Python and Matlab programming languages
            - Strong communication skills and experience working in team environments
            - Ability to work independantly
            - Eager to learn new concepts and skills quick
            """
            )
        
    with left_column:
        st_lottie(lottie_program, height=300)

# Significant Projects

with st.container():
    st.write("- - - ")
    st.title("Significant Projects")
    st.text("")
    st.text("")
    st.text("")

#with st.container():
    #st.write("- - - ")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Covid 19 Sensor")
        st.write("""
        A school project displaying my experience with coding
        - Constructed a sensor with Tinkercad software
        - Programmed Sensor using Arduino language
        - Designed a detailed schematic diagram of the sensor)
        """
        )
    with right_column:
        st.video("https://youtu.be/cCClXiONBHY")

   # Arduino Robot 

    left_column, right_column = st.columns(2)
    with left_column:
        st.text("")
        st.text("")
        st.header("Moving Arduino Robot")
        st.write("""
        A school project displaying my experience with coding
        - Created a chip from scratch 
        - Constructed a moving robot and connected the chip
        - Programmed the chip using arduino)
        """
        )
    with right_column:
        st.text("")
        st.text("")
        st.text("")
        st.video("https://youtu.be/Umkd1xdC1NQ")

    # Astro Wars

    with right_column:
        # Space out lines
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")

        #write title and description
        st.header("Beach Battles")
        st.write("Created Beach Battles game using pygame library")
        st.write("Users are able to move tank around the beach using keyboard")
        st.write("Users can shoot enemy, where enemy then disappears")
        st.write("Score increases as more enemies are eliminated")
        st.write(("[See Beach Battles Code >](https://github.com/UJcodez/Beach-Battles)"))
    
    with left_column:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st_lottie(lottie_boat, height=500, width=500)

    # Python Game Two

        with left_column:
        # Space out lines
            st.text("")
            st.text("")

        #write title and description
        st.header("Astro Wars - Python Game")
        st.write("Created Astro Wars game using pygame library")
        st.write("Two player game using keyboard")
        st.write("Users can move spaceships around and shoot at other player's ship")
        st.write("Scores are displayed and increase when player hits target")
        st.write(("[See Astro Wars Code >](https://github.com/UJcodez/Astro-Wars)"))
    
    with right_column:
        st.text("")
        st_lottie(lottie_space, height=400, width=500)
       

with st.container():
    st.write("- - -")

st.title("Contact :e-mail:")
st.text("")
st.write(("[Linkedin](https://www.linkedin.com/in/usayd-jahangiri-a685b0225/)"))
st.write(("[Github](https://github.com/UJcodez)"))
st.write(("[Youtube](https://www.youtube.com/channel/UCEr3s4IYdVxDQnF7S9XnGjA)"))





        










