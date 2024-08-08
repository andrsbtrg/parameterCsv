import streamlit as st
import parameters

def generateFile():
    pass

st.header("Hello")

output = ""


with st.container():
    uploaded_files = st.file_uploader("Upload csv files", type=["csv"], accept_multiple_files=True, on_change=generateFile )

    if st.button("Generate Unique Parameters") and len(uploaded_files) > 0:
        output = parameters.extract(uploaded_files)
    
    if output:
        st.download_button("Download Unique Parameters CSV", data=output, file_name="unique_parameters.csv", mime="text/csv")