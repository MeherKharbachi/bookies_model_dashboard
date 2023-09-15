import pandas as pd
#import plotly.express as px
import streamlit as st
from pathlib import Path
import io
from PIL import Image


st.set_page_config(layout="wide")

st.title("💾 Our Data")


def sidebar_multiselect_container(massage, arr, key):
    
    container = st.sidebar.container()
    select_all_button = st.sidebar.checkbox("Select all for " + key + " plots")
    if select_all_button:
        selected_num_cols = container.multiselect(massage, arr, default = list(arr))
    else:
        selected_num_cols = container.multiselect(massage, arr, default = arr[0])

    return selected_num_cols    

def df_isnull(df):
    res = pd.DataFrame(df.isnull().sum()).reset_index()
    res['Percentage'] = round(res[0] / df.shape[0] * 100, 2)
    res['Percentage'] = res['Percentage'].astype(str) + '%'
    return res.rename(columns = {'index':'Column', 0:'Number of null values'})

def df_info(df):
    df.columns = df.columns.str.replace(' ', '_')
    buffer = io.StringIO() 
    df.info(buf=buffer)
    s = buffer.getvalue() 

    df_info = s.split('\n')

    counts = []
    names = []
    nn_count = []
    dtype = []
    for i in range(5, len(df_info)-3):
        line = df_info[i].split()
        counts.append(line[0])
        names.append(line[1])
        nn_count.append(line[2])
        dtype.append(line[4])

    df_info_dataframe = pd.DataFrame(data = {'#':counts, 'Column':names, 'Non-Null Count':nn_count, 'Data Type':dtype})
    return df_info_dataframe.drop('#', axis = 1)


## import data 
df = pd.read_csv("./data/fixtures.csv")

st.subheader('Dataframe:')

n, m = df.shape

st.write(f'<p style="font-size:130%">Dataset contains {n} rows and {m} columns.</p>', unsafe_allow_html=True)  
st.dataframe(df)

all_vizuals = ['Info', 'NA Info', 'Descriptive Analysis', 'Count Plots of Categorical Columns']


for _ in range(3):
        st.sidebar.write("")

vizuals = st.sidebar.multiselect("Choose which visualizations you want to see 👇", all_vizuals)


if 'Info' in vizuals:
        st.subheader('Info:')
        c1, c2, c3 = st.columns([1, 2, 1])
        c2.dataframe(df_info(df))


if 'NA Info' in vizuals:
     st.subheader('NA Value Information:')
     if df.isnull().sum().sum() == 0:
          st.write('There is not any NA value in your dataset.')
     else:
          c1, c2, c3 = st.columns([0.5, 2, 0.5])
          c2.dataframe(df_isnull(df), width=1500)



if 'Descriptive Analysis' in vizuals:
     st.subheader('Descriptive Analysis:')
     st.dataframe(df.describe())


num_columns = df.select_dtypes(exclude = 'object').columns
cat_columns = df.select_dtypes(include = 'object').columns

if 'Count Plots of Categorical Columns' in vizuals:

     if len(cat_columns) == 0:
          st.write('There is no categorical columns in the data.')
     else:
          selected_cat_cols = sidebar_multiselect_container('Choose columns for Count plots:', cat_columns, 'Count')
          st.subheader('Count plots of categorical columns')
          i = 0
          while (i < len(selected_cat_cols)):
               c1, c2 = st.columns(2)
               for j in [c1, c2]:

                    if (i >= len(selected_cat_cols)):
                         break

                    fig = px.histogram(df, x = selected_cat_cols[i], color_discrete_sequence=['indianred'])
                    j.plotly_chart(fig)
                    i += 1


st.subheader('Games Bookies Odds:')

st.write("##### Using our own extraction tool, we retrieved bookmakers' odds from the Oddsportal website for each game listed above. In this regard, We obtained the 1x2, Asian handicap, total goals, and correct score odds.")
st.write("##### We have to note that, during the modelling phase, the user has the option of selecting the bookmaker of his choosing.")

tab_1x2, tab_asian, tab_over_under, tab_score = st.tabs(["1X2","Asian Handicap","Total Goals","Correct Score"])


with tab_1x2:
     st.write('# \n #')
     img = Image.open("pages/images/1x2_grid.png")
     st.image(img, width=1000)
     st.write('# \n #')

with tab_asian:
     st.write('# \n #')
     img = Image.open("pages/images/asian_grid.png")
     st.image(img, width=1000)
     st.write('# \n #')
with tab_over_under:
     st.write('# \n #')
     img = Image.open("pages/images/over_under_grid.png")
     st.image(img, width=1000)
     st.write('# \n #')
with tab_score:
     st.write('# \n #')
     img = Image.open("pages/images/correct_score_grid.png")
     st.image(img, width=1000)
     st.write('# \n #')
     img_2 = Image.open("pages/images/correct_score.png")
     st.image(img_2, width=1000)
     