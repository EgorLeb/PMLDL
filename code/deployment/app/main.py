import streamlit as st
import requests


st.title('Blond hair recognition')
cols = st.columns(2)
uploaded_file = None
with cols[0] as col:
    uploaded_file = st.file_uploader("")
    if uploaded_file:
        s = uploaded_file.name.split(".")
        if len(s) >= 2 and s[-1] in ["jpeg", "png", "jpg"]:
            bytes_data = uploaded_file.getvalue()
            st.image(bytes_data, uploaded_file.name)
with cols[1] as col:
    if uploaded_file:
        s = uploaded_file.name.split(".")
        if len(s) >= 2 and s[-1] in ["jpeg", "png", "jpg"]:
            bytes_data = uploaded_file.getvalue()
            url = 'http://fastapi:8000/upload'
            file = {'file': bytes_data}
            resp = requests.post(url=url, files=file, data={"filename": uploaded_file.name})
            st.title(" ")
            st.title(resp.json()["message"])
        else:
            st.title('Choose file with format ("jpeg", "png", "jpg")')
