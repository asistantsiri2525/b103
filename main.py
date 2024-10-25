
import numpy as np
import pandas as pd
import streamlit as st
from streamlit import line_chart, bar_chart, columns

st.title("THIS IS YOUR FIRST APPLICATION")
st.write("this is an just application!!!")


data=pd.DataFrame({
    "name":["Tejas","Tejaswini","Sanket","Ram","riye"],
      "marks":[40,70,89,77,55]
})
st.write("detalis of students are given below:")
st.write(data)


chart_data=pd.DataFrame(
    np.random.rand(20,5),columns=['A','B','C','D','E']
)

st.line_chart(chart_data)

st.bar_chart(chart_data)





