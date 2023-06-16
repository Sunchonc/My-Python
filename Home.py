from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


st.header('Natthasut & Nirut')
st.image("./pic/Me.jpg")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("./pic/Iris1.jpg")

with col2:
   st.header("Verginiga")
   st.image("./pic/Iris2.jpg")

with col3:
   st.header("Setosa")
   st.image("./pic/Iris3.jpg")

   html_8 = """
<div style="background-color:#EC7063;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

pt_len = st.slider("กรุณาเลือกข้อมูล petal.length")
pt_wd = st.slider("กรุณาเลือกข้อมูล petal.width")

sp_len = st.number_input("กรุณาเลือกข้อมูล sepal.length")
sp_wd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

if st.button("ทำนายผล"):
    st.markdown("ทำนาย")
else:
    st.write("ไม่ทำนาย")