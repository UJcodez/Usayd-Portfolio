## Website 
import json
import requests
import streamlit as st
from PIL import Image


st.set_page_config(page_title="Usayd's Webpage", page_icon=":tada:", layout="wide")

# Header
with st.container():
    st.subheader("Welcome to my personal website :wave:")
    st.title("A future computer engineer studying at TMU")
    st.write("I have designed this website to demostrate my capabilities and understanding of code")
    st.write("[My Resume >](file:///C:/Users/Test/Downloads/White%20Gold%20Elegant%20Minimalist%20ATS%20Data%20Analyst%20Resume%20CV%20A4%20Printable%20(2).pdf)")

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
            - Current GPA: TBD (Semester 1)
            - Studying both software and hardware systems
            - Significant courses include: Programming Fundamentals, Electric Circuit Analysis, Engineering Economics

            """
            )

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
       

# Significant Projects

with st.container():
    st.write("- - - ")
    st.title("Significant Projects")
    st.text("")
    st.text("")
    st.text("")

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

    # Python Game Two

        with left_column:
        # Space out lines
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
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
        
       

with st.container():
    st.write("- - -")

st.title("Contact :e-mail:")
st.text("")
st.write(("[Linkedin](https://www.linkedin.com/in/usayd-jahangiri-a685b0225/)"))
st.write(("[Github](https://github.com/UJcodez)"))
st.write(("[Youtube](https://www.youtube.com/channel/UCEr3s4IYdVxDQnF7S9XnGjA)"))





        










