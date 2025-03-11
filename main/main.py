import pandas as pd
import numpy as np

import streamlit as st
from streamlit_drawable_canvas import st_canvas

from database import add, extract
from classifier import load_model, predict

if "prediction" not in st.session_state:
    st.session_state["prediction"] = " "
    st.session_state["confidence"] = " "

if "model" not in st.session_state.keys():
    st.session_state["model"] = load_model()
    model = st.session_state["model"]

if "records" not in st.session_state.keys():
    st.session_state["records"] = pd.DataFrame(extract(),columns=["Timestamp","Prediction","Label"]).sort_values(by="Timestamp",ascending= False)
records = st.session_state["records"]

def inference(canvas):
    im = 255 - np.mean(canvas.image_data[:,:,0:3],axis = 2)
    st.session_state["prediction"], st.session_state["confidence"] = predict(im)

def log(value):
    add(st.session_state["prediction"],value)
    st.session_state["records"] = pd.DataFrame(extract(),columns=["Timestamp","Prediction","Label"]).sort_values(by="Timestamp",ascending= False)

def main():
    st.title("Digit Classifier")
    c1,c2,c3 = st.columns(3)
    # Set up the canvas
    with c1:
        canvas = st_canvas(
            width=224,
            height=224,
            stroke_width=16,  # Brush thickness
            stroke_color="black",  # Brush color
            background_color="white",
            drawing_mode="freedraw",
        )
    with c2:
        st.text("Prediction: " + st.session_state["prediction"])
        st.text("Confidence: " + st.session_state["confidence"])
        st.button(label = "Predict",on_click=inference,args = (canvas,))
    with c3:
        d1,d2 = st.columns(2)
        with d1:
            correction = st.text_area(label = "True label:",height = 68)
            st.button(label = "Log",on_click=log,args = (correction,))
    st.header("History")
    st.table(records)

main()
