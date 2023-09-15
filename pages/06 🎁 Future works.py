import streamlit as st
from PIL import Image


st.title("🎁 Future work")

st.write('# \n #')
img = Image.open("pages/images/future-work.jpg")
st.image(img, width=1200)
st.write('# \n #')



r"""
* Fine Tuning: select (by trial and error on validation set):
  * Number of hidden layers
  * Number of Neurons
  * Amount of distillation i.e α (alpha)
  * Important of each loss: weights W_1, W_2, W_3, W_4
* More distillation: use more bookmaker lines (asian and total mainly) to transfer more knowledge
"""








