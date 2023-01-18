import streamlit as st
import pandas as pd


view = [100, 150, 30]

st.write("# test1")
st.write("## test2")
view
st.write("## test3")
st.bar_chart(view)

sview = pd.Series(view)
sview

