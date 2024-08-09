import streamlit as st
import parameters

st.header("Unique parameters")

output = ""

ignore_groups = []

with st.container():
    ignore_params = st.text_input("Write the group names to ignore, separated by space"
                                  , value="ANALYTICAL_PROPERTIES IFC DATA")
    if st.button("Validate Ignore Groups"):
        ignore_groups = ignore_params.split(" ")
        st.write("Your will ignore " + str(len(ignore_groups)) + " groups:")
        ignore_groups

with st.container():
    uploaded_files = st.file_uploader("Upload csv files", type=["csv"], accept_multiple_files=True)

    if st.button("Generate Unique Parameters") and len(uploaded_files) > 0:
        ignore_groups = ignore_params.split(" ")
        output = parameters.extract(uploaded_files, ignore_groups)
    
    if output:
        st.download_button("Download Unique Parameters CSV", data=output, file_name="unique_parameters.csv", mime="text/csv")