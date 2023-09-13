import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

st.title("🔨 Breaking a model")

tab1, tab2, tab3 = st.tabs(["Model Structure", "Model Loss", "Model Training"])
with tab1:
    
    st.header('''Model structure''')

    
    st.write('''A simple multilayer perceptron (MLP) network inspired from fastai tabular learner.
            \n - **Categorical variables:** Categorical variables (here competition ID) are passed through an embedding layer followed by a dropout layer.
            \n - **Continuous variables:**  Continuous variables are first concatenated with the transformed categorical variables (i.e, after embedding) passed to a custom layer which is a succession of batch normalization, dropout and a linear layer.            
            ''')

    st.write('# \n #')
    img = Image.open("pages/images/model_architecture.png")
    st.image(img, width=1000)
    st.write('# \n #')


with tab2:

    st.header('''Model Loss''')

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
    st.image(img, width=1000)
    st.write('# \n #')


with tab3:

    st.header('''Model Training''')
    st.write('''
    In this section, we will describe how we have trained our model.         
    ''') 

    st.subheader('''Data splitting''')
    
    st.write('''We divided our 24k rows into **80%** training data and **20%** validation and test data. We must emphasise that we have stratified our inputs based on the competition name in order to get balanced observations.''') 


    st.subheader('''Checkpoints''')
    
    st.write('''

    To train our model, we set up **Pytorch Lightning** model checkpoint and **Early stopping** to save the best trails and stop training before overfitting.

    ''') 

    st.subheader('''Loss Monitoring''')
    
    combined_loss, combined_loss_1x2 = st.tabs(["Global Combined Loss","1X2 Combined Loss"])
 
    with combined_loss:
        
        st.write('''

        In this experiment, we will monitor the global combined loss mentioned in the later tab using different scenarios:

        ''') 

        st.write(''' 
        - **Equal weights:** Here weights will be equal to 0.25. Balanced performance , all the markets are equally important in our optimization procees. it means the model will have a broad understanding of the four markets.
        \n - **Equal weights + alpha = 0.3:** with an alpha = 0.3 , the model will give more importance to the hard loss component (for the 4 losses), we expect better results in predicting real outcomes but maybe weaker alignment with bookies odds
        \n - **Equal weights + alpha = 0.7:** with an alpha = 0.7 , the model will give more importance to the KL divergence component (for the 4 losses), we expect better alignment with bookies but it could be not accurate in predicting real outcomes
        \n - **Higher priority for score loss:** it will place greater emphasis on scores preds with no solid knowledge of the other markets , with a weight of 0.5 .
        \n - **Higher priority for score loss + alpha= 0.3:** the model will give more importance to the hard loss component with more importance on score loss.
        \n - **Higher priority for score loss + alpha= 0.7:** the model will give more importance to the KL loss component with more importance on score loss.
        ''')


    with combined_loss_1x2:
        
        st.write('''
            In this experimentation, we will monitor the 1X2 combined loss described in the latter tab, with different scenarios:
        ''') 

        st.write(''' 
        - **Alpha= 0.5 :** try with an alpha equal to 0.5
        \n - **Alpha= 0.3 :** try with an alpha equal to 0.3
        \n - **Alpha = 0.7:** try with an alpha equal to 0.7
        ''')





