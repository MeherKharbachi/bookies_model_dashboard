import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")


## about the project section
st.markdown("""# About The Project""")
st.write("""#""")
st.write("##### In this project, we will use the concept of knowledge distillation to steal the model established by sports betting bookies.")
st.write("##### In this way, the learner will identify patterns through the probabilities of the provided markets such as 1X2, Asian Handicap, and Over/Under which will lead our model to replicate the original model and use it as a benchmark in future projects.")

st.write("""# \n ##""")

## what is KD section
st.subheader(
    """*What is Knowledge Distillation:* """)

st.write(''' - **Knowledge Transfer:** Knowledge distillation is a technique where a smaller neural network (student) learns from a larger, more complex one (teacher) to mimic its knowledge.
        \n - **Model Compression:** making deep neural networks more efficient by transferring the essential information from the teacher to the student model.
        \n - **Temperature Scaling:** The teacher provides softened probabilities (logits) to the student, often through a temperature scaling factor, making it easier for the student to learn the complex decision boundaries.
        \n - **Improved Efficiency:**  Knowledge distillation allows for smaller, faster, and less resource-intensive models while maintaining competitive performance, crucial for applications with limited computational resources. 
        \n - **Loss Components:** The loss function in knowledge distillation often consists of two components:
        \n      - **Hard Target Loss:** standard cross-entropy loss between the student's predictions and the true labels.
        \n      - **Soft Target Loss:**  the divergence between the student's predictions and the teacher's softened predictions.
         
        ''')

st.latex(r'''
         Loss = \alpha \times Hard\_Target\_Loss +  (1-\alpha) \times Soft\_Target\_Loss
    ''')


## Image section
st.write('# \n #')
img = Image.open("pages/images/kd_graph.png")
st.image(img, width=1000)
st.write('# \n #')


## Github Link section
st.subheader(
        """**Github Repo code:** """)
st.subheader("""
🔗 :blue[github.com/real-analytics-rd/bookies_model]"""
)
