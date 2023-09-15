import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

st.title("🔨 The Model")

st.write('# \n #')

st.markdown("# Why Neural Network ?")
st.write('# \n #')
img = Image.open("pages/images/The-Universal-Approximation-Theorem.png")
st.image(img, width=1400)


st.write('# \n #')
st.header('''Model structure''')
st.write('''A simple multilayer perceptron (MLP) network inspired from fastai tabular learner.
        \n - **Categorical variables:** Categorical variables (here competition ID) are passed through an embedding layer followed by a dropout layer.
        \n - **Continuous variables:**  Continuous variables are first concatenated with the transformed categorical variables (i.e, after embedding) passed to a custom layer which is a succession of batch normalization, dropout and a linear layer.            
        ''')

st.write('# \n #')
img = Image.open("pages/images/model_architecture.png")
st.image(img, width=1400)
st.write('# \n #')



st.header('''Training''')
st.write('''We established several kinds of losses that we may use to train our model.Using the expected score matrix, we first extract the 1x2, Asian, and total objectives probabilities, then we define the following losses for each market:
        \n - **Hard loss:** The log loss of the predicted market probas for the observed match result
        \n - **KL loss:**   The divergence between the predicted market vs bookies probas.            
        \n - **Combined loss:**   Combine the above losses.                        
            ''')

st.write('''

        After computing all of the losses indicated above, we have calculated a global aggregate loss for the whole market:

''') 
st.latex(r'''
        global\_Loss = W_1 \times score\_combined\_Loss +
            W_2 \times 1x2\_combined\_Loss +
            W_3 \times Asian\_combined\_Loss +
            W_4 \times Total\_Goals\_combined\_Loss
''')

st.write('''
With :
        \n   W_i : Importance Weights
''') 

st.write('# \n #')
img = Image.open("pages/images/loss.png")
st.image(img, width=1400)





