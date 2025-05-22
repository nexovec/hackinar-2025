import streamlit as st

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

# zpracuj data
st.sidebar.markdown(f"Továrna na jsoucno, chrám boží, v0.1")
