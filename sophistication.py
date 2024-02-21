import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Sophistication", layout="centered")
 
st.subheader("Sophistication") 
st.write("better A.I.") 
st.write("---")

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "about","Terms and policy of privacy","Contact"],
    )

if selected == "Home":
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://giphy.com/gifs/garden-ZuhhRTIUFF00U")
    }

    [data-testid=stHeader] {
    Background-color: rgba(0, 0, 0, 0);
    }

    [data-testid="stToolbar"] {
    right: 2rem;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True,)
    st.title("About:")
    st.write("Hello, :wave:")
    st.write("Hello from the samuna family where we make all use, all organic,non toxic,and non alchoolic soap.")
    st.write("   ")
    st.write("samuna is a startup e-commerce,and retail company that sells quality, and organic all use soap.")
   
a="https://buy.stripe.com/test_28o5m05fIgRy5dmfYZ"
