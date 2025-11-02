import streamlit as st

st.set_page_config(
    page_title="Objective 1"
)

# Using HTML for styling
st.markdown(
    """
    <style>
    .title {
        background-color: #f0f0f0; /* Light gray background */
        color: #333333; /* Dark text color */
        padding: 10px; /* Padding around the text */
        border-radius: 5px; /* Rounded corners */
        border: 2px solid #cccccc; /* Border color */
        text-align: center; /* Centered text */
    }
    </style>
    <div class="title">
        <h1>Objective 1</h1>
    </div>
    """,
    unsafe_allow_html=True
)
