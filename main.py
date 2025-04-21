import streamlit as st
import pandas as pd

#pip3 install -r requirements.txt
#streamlit run main.py

df=pd.read_csv('/Users/apple/Documents/Guvi/AWS Clould/hosting_app/crop_production_prime_new-2.csv')
show_df=df.head()
st.title("Sample for hosting")
st.write("Ellie How are you")
st.dataframe(show_df)
