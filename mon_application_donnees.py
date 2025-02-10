import streamlit as st
import pandas as pd


st.markdown("<h1 style='text-align: center; color: black;'>MY DATA APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app allows you to download scraped data on ordinateurs, telephones and tv home cinema from expat-dakar 
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).


""")
KOBO_FORM_URL = "https://kf.kobotoolbox.org/#/forms/abZk8yQA2bFNni3KGHn8Rb"

st.title("Formulaire d'évaluation d'un application KoboToolbox intégré à Streamlit")
st.markdown(
    f'<iframe src="{KOBO_FORM_URL}" width="100%" height="600"></iframe>',
    unsafe_allow_html=True
)





# Fonction de loading des données
def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

          
# Charger les données 
load_(pd.read_csv('data/oridinateurs_data_scrape.csv'), 'Ordinateurs data 1', '1')
load_(pd.read_csv('data/telephone_data_scrape.csv'), 'Telephones data 2', '2')
load_(pd.read_csv('data/tv_home_cinema_data_scrape.csv'), 'TV Home Cinema 3', '3')





 


