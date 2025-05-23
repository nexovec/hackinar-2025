import streamlit as st
import requests

# API endpoint
API_URL = "http://localhost:8000/api/files/upload"

# pár konfiguračních věcí na začátek, v prezentaci přeskočíme
streamlit_menu_items = {
    # "Get help": "<url>",
    # 'Report a bug': "<url>",
    # 'About': "<url>",
}
st.set_page_config("Streamlit workshop", layout="wide", initial_sidebar_state="expanded", page_icon="🚗", menu_items=streamlit_menu_items)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Zobraz data")
st.sidebar.title("Navigace")

# Náhradní část
# File upload widget
st.sidebar.markdown("### Upload souboru")
uploaded_file = st.sidebar.file_uploader("Vyberte soubor", type=None)

if uploaded_file is not None:
    # Prepare the request
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    data = {"filename": uploaded_file.name.split(".")[0]}
    
    try:
        response = requests.post(API_URL, files=files, data=data)
        response.raise_for_status()
        st.sidebar.success("Soubor úspěšně nahrán!")
        st.sidebar.json(response.json())
    except requests.exceptions.RequestException as e:
        st.sidebar.error(f"Chyba při nahrávání souboru: {str(e)}")

def show_debug_info():
    try:
        response = requests.get("http://localhost:8000/debug/all")
        response.raise_for_status()
        debug_data = response.json()
        
        st.subheader("Debug Information")
        if debug_data:
            for item in debug_data:
                st.json(item)
        else:
            st.info("No debug data available")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching debug data: {str(e)}")

def list_filenames():
    try:
        response = requests.get("http://localhost:8000/api/files/list_filenames")
        response.raise_for_status()
        data = response.json()
        
        st.subheader("Uploaded Files")
        st.json(data)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching file list: {str(e)}")

# zpracuj data
st.sidebar.markdown(f"Továrna na jsoucno, chrám boží, v0.1")
show_debug_info()
list_filenames()
