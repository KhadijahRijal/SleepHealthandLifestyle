import streamlit as st

st.set_page_config(
    page_title="Objective 1"
)

# Using HTML for styling with a gradient box
st.markdown(
    """
    <style>
    .title {
        background: linear-gradient(90deg, #ff69b4, #8a2be2, #00bfff); /* Gradient from pink to purple to blue */
        color: #ffffff; /* White text color */
        padding: 10px; /* Padding around the text */
        border-radius: 5px; /* Rounded corners */
        border: 2px solid transparent; /* No border, or set to transparent */
        text-align: center; /* Centered text */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5); /* Shadow for depth */
    }
    h1 {
        margin: 0; /* Remove default margin */
    }
    </style>
    <div class="title">
        <h1>Objective 1</h1>
    </div>
    """,
    unsafe_allow_html=True
)
