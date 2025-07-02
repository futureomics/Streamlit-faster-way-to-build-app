#✅ 1. Install Streamlit
#Open your terminal or command prompt and run:
#bash

#pip install streamlit
#pip install streamlit

#✅ 2. Create a Simple Streamlit App
#Create a Python file (e.g. app.py) with this content:

import streamlit as st

st.title("Simple Streamlit App")

name = st.text_input("FutureOmics:")
if name:
    st.write(f"Hello, {name} 👋")


#✅ 3. Run the Streamlit App Locally
#Run this command in the terminal (in the folder where app.py is saved):

#bash

streamlit run app.py

This will open your app in the browser at http://localhost:8501.
