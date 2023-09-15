import streamlit as st
from PIL import Image

st.set_page_config(
    layout="wide",
)


col1, col2 = st.columns([9,5])

with col1:


    st.write('#')
    st.write('#')
    st.write('#')
    st.markdown('''# Steal The Bookies''')
    st.markdown('''# 🍯😊⛏️🐍🔥🧮''')

    st.write('#')

    st.markdown('''## How Can We Learn Bookmakers Model From The Main Markets Using Machine Learning ?''')

with col2:
    image = Image.open("pages/images/stealing-front.png")
    st.image(image, width = 600)
