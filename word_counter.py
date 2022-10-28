from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title("Word usage counter")

text = st.text_input('Copy and paste the text', 'Paste here')


text= str(text)
data = []
#gets text or csv file and counts every words occurance and prints
d = dict()

text = text.strip()
text = text.lower()
words = text.split(" ")

for word in words:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

for key in list(d.keys()):
    data += [{"words": key,"number": d[key]}]
        
df = pd.DataFrame(data)

if df.empty == False:
    df = df.sort_values("number", ascending=False)
    df = df.reset_index()
    del df['index']
    col1, col2 = st.columns([2, 1])
    col1.subheader("Words chart /excluded 1s")
    df1 = df[df["number"] > 1]
    col1.bar_chart(df1,x="words", y="number")
#, width=0, height=0, use_container_width=True)

    col2.subheader("Words data")
    col2.write(df)
        
