import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import io

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
        if data['filenames']:
            selected = st.selectbox(
                "Select an uploaded file",
                data['filenames'],
                index=0,
                help="Choose a file to work with"
            )
            
            # Download and display selected file
            try:
                response = requests.get(f"http://localhost:8000/api/files/download/{selected}")
                response.raise_for_status()
                st.subheader("File Content")
                st.code(response.content.decode('utf-8'), language='text')
                
                # Load CSV into pandas and display with Plotly
                try:
                    df = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
                    st.subheader("CSV Data Visualization")
                    
                    # Show dataframe preview
                    st.write("Data Preview:")
                    st.dataframe(df.head())
                    
                    # Let user select columns
                    cols = df.columns.tolist()
                    if cols:
                        col1, col2 = st.columns(2)
                        with col1:
                            x_col = st.selectbox("X Axis", options=cols, index=0)
                        with col2:
                            y_col = st.selectbox("Y Axis", options=cols, index=min(1, len(cols)-1))
                        
                        # Create interactive plot with selected columns
                        try:
                            fig = px.line(df, x=x_col, y=y_col, 
                                        title=f"{y_col} vs {x_col} in {selected}",
                                        labels={x_col: x_col, y_col: y_col})
                            st.plotly_chart(fig)
                        except Exception as plot_error:
                            st.error(f"Error creating plot: {str(plot_error)}")
                    else:
                        st.error("No columns found in the CSV file")
                    
                except Exception as e:
                    st.error(f"Error processing CSV: {str(e)}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error downloading file: {str(e)}")
        else:
            st.warning("No files uploaded yet")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching file list: {str(e)}")

# zpracuj data
st.sidebar.markdown(f"Továrna na jsoucno, chrám boží, v0.1")
show_debug_info()
list_filenames()
