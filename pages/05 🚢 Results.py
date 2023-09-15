import streamlit as st
from pathlib import Path
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")

st.title("🚢 Results")
alpha = 0.3
market = st.sidebar.selectbox(
    'Select a market',
    ('1x2', 'asian', 'over_under',"score"))


st.markdown("🚢 Initial Results")

st.write('''

In the best experiment, we have monitored the global combined loss mentioned in the later slide using an alpha equal to 0.3 and different weight values:

''') 

is_equal = "not_equal"
image_path_train = f"{is_equal}_{alpha}_train.png"
image_path_valid = f"{is_equal}_{alpha}_valid.png"
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

img_2 = Image.open("pages/images/learned.jpg")
st.image(img_2, width=700)

if market != "score":
        
        test_market = pd.read_csv(f"./data/test_{market}.csv")
        valid_market = pd.read_csv(f"./data/valid_{market}.csv")
        st.write('# \n #')
        st.write('# \n #')


        if market == "1x2":
                st.markdown("## 1X2 Log Loss")

                col1, col2 = st.columns(2)
                st.write('# \n #')
                st.write('# \n #')
                col1.metric("Log Loss 1X2 Model Validation", value = round(valid_market["log_loss_1x2_model"].mean(),3))
                col1.metric("Log Loss 1X2 Model Test", value = round(test_market["log_loss_1x2_model"].mean(),3))
                col2.metric("Log Loss 1X2 Bookies Validation", value = round(valid_market["log_loss_1x2_bookies"].mean(),3))
                col2.metric("Log Loss 1X2 Bookies Test", value = round(test_market["log_loss_1x2_bookies"].mean(),3))



        else:
                st.markdown(f"## {market.capitalize()} Log Loss")
                test_log_loss_asian = test_market.groupby(f'{market}_line').agg({f'log_loss_{market}_model': 'mean', f'log_loss_{market}_bookies': 'mean'})
                test_log_loss_asian['Number of observations'] = test_market.groupby(f'{market}_line')[f'{market}_line'].count()
                test_log_loss_asian['Winner'] = test_log_loss_asian.apply(lambda row: "Bookies" if row[f'log_loss_{market}_model'] > row[f'log_loss_{market}_bookies'] else "Model", axis=1)
                test_log_loss_asian['Bookmaker'] = "Bet365"
                
                valid_log_loss_asian = valid_market.groupby(f'{market}_line').agg({f'log_loss_{market}_model': 'mean', f'log_loss_{market}_bookies': 'mean'})
                valid_log_loss_asian['Number of observations'] = valid_market.groupby(f'{market}_line')[f'{market}_line'].count()
                valid_log_loss_asian['Winner'] = valid_log_loss_asian.apply(lambda row: "Bookies" if row[f'log_loss_{market}_model'] > row[f'log_loss_{market}_bookies'] else "Model", axis=1)
                valid_log_loss_asian['Bookmaker'] = "Bet365"


                st.markdown(f"### Test Log Loss")
                st.dataframe(test_log_loss_asian)
                st.write('# \n #')
                st.markdown(f"### Validation Log Loss")
                st.dataframe(valid_log_loss_asian)


                

st.write('# \n #')
st.subheader("""Are We Close to Bookmakers ??""")





