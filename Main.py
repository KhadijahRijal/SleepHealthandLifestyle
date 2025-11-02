import streamlit as st

st.set_page_config(
    page_title="Objective 1"
)

# Using HTML for styling with a gradient box
st.markdown(
    """
    <style>
    .title {
        /*
          Darker Gradient:
          Using deep jewel tones: Dark Ruby (#8b0000) -> Deep Indigo (#4b0082) -> Navy Blue (#000080)
          This creates a richer, more saturated, and darker look.
        */
        background: linear-gradient(90deg, #8b0000, #4b0082, #000080); /* Dark Gradient */
        color: #ffffff; /* White text color for high contrast */
        padding: 10px;
        border-radius: 5px;
        border: 2px solid transparent;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.7); /* Stronger shadow for depth */
    }
    h1 {
        margin: 0;
    }
    </style>
    <div class="title">
        <h1>Objective 1</h1>
    </div>
    """,
    unsafe_allow_html=True
)
