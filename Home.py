import streamlit as st
from PIL import Image

st.set_page_config(
    layout="wide",
)


col1, col2 = st.columns([6,5])

with col1:


    st.write('#')
    st.write('#')
    st.write('#')
    st.markdown('''# Knowledge Distillation''')
    st.markdown('''# 🍯😊⛏️🐍🔥🧮''')

    st.write('#')

    st.markdown('''## Bookies Model''')

with col2:
    st.write('#')
    st.write('#')
    st.write('#')
    st.write('#')
    st.write('#')
    st.write('#')
    st.write('#')
    image = Image.open("pages/images/RA.png")
    st.image(image, width = 500)
