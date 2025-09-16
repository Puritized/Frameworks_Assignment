
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Load data
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Sidebar filters
year_range = st.slider("Select year range", 2019, 2023, (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)

st.subheader("Word Cloud of Titles")
titles = " ".join(filtered['title'].dropna().tolist())
wc = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots()
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

st.subheader("Sample Data")
st.write(filtered.head())
