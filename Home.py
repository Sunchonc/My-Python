import streamlit as st

st.header('natthasut')

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