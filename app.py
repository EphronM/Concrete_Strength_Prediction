from matplotlib.pyplot import text
import streamlit as st
import pickle
import base64
from static.load_css import local_css
import numpy as np
local_css("static/style.css")

model_dir = 'artifacts\prediction_model.pkl'
model = pickle.load(open(model_dir, 'rb'))

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('artifacts/bg.jpg')

def center_text(text):
    text_mk = f"<center>{text}</center>"
    return st.sidebar.markdown(text_mk, unsafe_allow_html=True)  


main_title = "<center><div><p class='highlight grey' style='font-size:47px'><span class='bold'>Cement Strength Projection</span></span></div></center>"
st.markdown(main_title, unsafe_allow_html=True)

text = "<p class='highlight grey' style='font-size:15px'> Adjust the parameters to find the strength of the concrete mixture</p>"
st.markdown(text, unsafe_allow_html=True)

center_text('Age')
age = st.sidebar.slider('', 1, 350,135)
center_text('Cement')
cement = st.sidebar.slider('', 100, 500,303)
center_text('superplastic')
superplastic = st.sidebar.slider('', 0, 30,0)
center_text('water')
water = st.sidebar.slider('', 120, 200,133)
center_text('slag')
slag = st.sidebar.slider('', 0, 350,0)
center_text('fineagg')
fineagg = st.sidebar.slider('', 600, 1000,800)
center_text('ash')
ash = st.sidebar.slider('', 120, 200,170)
center_text('coarseagg')
coarseagg = st.sidebar.slider('', 800, 1100,950)


st.markdown('<br>', unsafe_allow_html=True)
if st.button('Predict strength'):
    pred = model.predict([[cement, slag, ash, water, superplastic, coarseagg, fineagg, age]])
    st.markdown('<br><br>', unsafe_allow_html=True)

    text = f"<center><div><span class='highlight result' style='font-size:25px'>concrete has strength of<span class='bold'> {np.round(pred[0],2)}</span>MPa</span></div></center>"
    st.markdown(text, unsafe_allow_html=True)

