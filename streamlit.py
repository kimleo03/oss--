import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.number_input('input number',0,10)
st.title("practice")
st.text_input('email')
st.date_input('date')
st.time_input('time(KOR)')
st.text_area('description')
st.file_uploader('upload photo')
st.color_picker('Choose color')