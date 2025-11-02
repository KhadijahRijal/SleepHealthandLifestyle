import streamlit as st

st.set_page_config(
    page_title="Objective 1"
)

# Using HTML for styling with a colorful dark theme
st.markdown(
    """
    <style>
    .title {
        background-color: #1e1e1e; /* Dark gray background */
        color: #ffffff; /* White text color */
        padding: 10px; /* Padding around the text */
        border-radius: 5px; /* Rounded corners */
        border: 2px solid #4b0082; /* Indigo border */
        text-align: center; /* Centered text */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5); /* Shadow for depth */
    }
    h1 {
        color: #ff69b4; /* Pink text */
        background: linear-gradient(90deg, #8a2be2, #00bfff); /* Gradient from purple to blue */
        -webkit-background-clip: text; /* Clip background to text */
        -webkit-text-fill-color: transparent; /* Fill text with gradient */
    }
    </style>
    <div class="title">
        <h1>Objective 1</h1>
    </div>
    """,
    unsafe_allow_html=True
)
