import streamlit as st
import pandas as pd

# Title of the app
st.set_page_config(page_title="Curated Knowledge Hub")
st.title("📚 My Curated Knowledge Hub")

# Load content
df = pd.read_csv("content.csv")

# Category filter
category = st.selectbox("Choose a category", ["All"] + df["Category"].unique().tolist())
if category != "All":
    df = df[df["Category"] == category]

# Display content
st.write(f"Showing {len(df)} items")
for i, row in df.iterrows():
    st.markdown(f"**[{row['Title']}]({row['Link']})** - {row['Category']}")

# Search content
search = st.text_input("Search Articles")
if search:
    df = df[df["Title"].str.contains(search, case=False)]