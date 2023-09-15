import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")


## Model Stealing concept
st.markdown("""# Model Stealing concept""")
st.write("""#""")

img = Image.open("pages/images/Stealing concept.png")
st.image(img, width=1000)
st.write(''' - The Data owner has trained a model and made its output (predictions) available as a service.
        \n - An Adversary is able to send inputs and receive outputs (usually as class probabilities) and pays per request.
        \n - The adversary is willing to replicate the behaviour of the model with high precision with minimum number of queries.
        ''')


st.markdown("""# Do You See A Similarity With Bookies?""")
img_2 = Image.open("pages/images/similarity.png")
st.image(img_2, width=1000)
st.write(''' - Bookies publish their odds (the Data owner).
        \n - Traders query the main markets.
        \n - We want our models to be calibrated (look like the bookie model) but also be accurate (reflect reality).
        ''')


st.markdown("""# Main Assumptions""")
img_3 = Image.open("pages/images/assumptions.png")
st.image(img_3, width=1000)
st.write(''' - Bookies use a model to produce their odds (safe).
        \n - Bookies model is informed by limited number of inputs (semi-safe).
        \n - These inputs can be approximated (inferred) from the observation of the main markets (semi-safe).
        ''')
st.write("""# \n ##""")