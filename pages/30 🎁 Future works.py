import streamlit as st

st.markdown("# 🎁 Future work")

st.header("""*Improving Model Distillation through Enhanced Bookmaker Data:* """)


st.write('''

In our pursuit of enhancing the model distillation process, we have identified a promising avenue for improvement by leveraging additional information provided by the bookmaker. Our objective is to not only rely on the liquid line data for Asian handicap and total goals markets but to expand our approach by incorporating a few lines around the liquid line.

The core concept behind this strategy is not to utilize these additional lines as direct inputs into our model but rather to harness them for the purpose of enriching the Knowledge Distillation divergence (KD) loss in a preliminary stage.
         
''') 


st.subheader("""*Enriched Knowledge Transfer:* """)

st.write('''
By including these extra lines in the Knowledge Distillation process, we aim to foster a more comprehensive understanding of the underlying dynamics in the Asian handicap and total goals markets.
While these additional lines may not directly influence the model's predictions, they serve as valuable contextual information that can aid in training.         
''') 


st.subheader("""*Improved Model Generalization:* """)

st.write('''
Expanding our focus beyond the liquid line enables our model to grasp a broader spectrum of market movements and fluctuations.
This can lead to improved generalization capabilities, allowing the model to make more accurate predictions on unseen data.''') 





