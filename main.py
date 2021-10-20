# Import necessary modules
import streamlit as st
from trending_repo import get_trend
from featured_topics import get_topic

# Give title to your stremlit page
st.title("Github Web Scrapping")

# Get the dataframe
trend_df = get_trend()
topic_df = get_topic()

# Create checkbox to show the data in the dataframe
check1 = st.checkbox("Show Github Trending Repository")
if check1:
    st.dataframe(trend_df)

check2 = st.checkbox("Show Github Featured Topics")
if check2:
    st.dataframe(topic_df)

