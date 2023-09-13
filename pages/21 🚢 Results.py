import streamlit as st
from pathlib import Path
from PIL import Image



for _ in range(3):
        st.sidebar.write("")


alpha = st.sidebar.slider(label = 'Select a value for alpha',
                            min_value=0.3,
                            max_value=0.7,
                            value=0.5,
                            step=0.2)

market = st.sidebar.selectbox(
    'Select a market',
    ('1x2', 'asian', 'over_under',"score"))


combined_loss, combined_loss_1x2 = st.tabs(["Global Combined Loss","1X2 Combined Loss"])

with combined_loss:

        st.write('''

        In this experiment, we will monitor the global combined loss mentioned in the later tab using different scenarios:

        ''') 

        weights = st.checkbox("Do you want to have equal weights")
        is_equal = "equal" if weights else "not_equal"
        image_path_train = f"{is_equal}_{alpha}_train.png"
        image_path_valid = f"{is_equal}_{alpha}_valid.png"

        st.write('# \n #')
        path_to_market_train = Path(f"pages/images/{market}_{image_path_train}")
        path_to_market_valid = Path(f"pages/images/{market}_{image_path_valid}")
        st.subheader("""*Training Curve:* """)
        img = Image.open(path_to_market_train)
        st.image(img, width=800)
        st.write('# \n #')
        st.subheader("""*Validation Curve:* """)
        img_2 = Image.open(path_to_market_valid)
        st.image(img_2, width=800)
        st.write('# \n #')

with combined_loss_1x2:

        st.write('''
                In this experimentation, we will monitor the 1X2 combined loss described in the latter tab, with different scenarios:
        ''') 

        st.write('# \n #')
        path_to_market_train = Path(f"pages/images/{market}_1x2_combined_{alpha}_train.png")
        path_to_market_valid = Path(f"pages/images/{market}_1x2_combined_{alpha}_valid.png")
        st.subheader("""*Training Curve:* """)
        img = Image.open(path_to_market_train)
        st.image(img, width=800)
        st.write('# \n #')
        st.subheader("""*Validation Curve:* """)
        img_2 = Image.open(path_to_market_valid)
        st.image(img_2, width=800)
        st.write('# \n #')


