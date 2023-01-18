import streamlit as st
import pandas as pd
import random


view = [100, 150, 30]

st.write("# test1")
st.write("## test2")
view
st.write("## test3")
st.bar_chart(view)

i = 0
view_1 = []

while True:
  
  if i > 10:
    break
  
  view_1.append(random.randint(0,10))
  sview = pd.Series(view_1)
  
  st.bar_chart(view_1)

  i += 1
