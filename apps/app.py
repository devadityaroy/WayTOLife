import heart
import kidney
import exercise
import diabetes
import streamlit as st


PAGES = {
    "Heart Diesease Detection": heart,
    "Kidney Diesease Detection": kidney,
    "Diabetes Diesease Detection": diabetes,
    "Exercise": exercise
}
st.sidebar.title('NAVIGATION')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()