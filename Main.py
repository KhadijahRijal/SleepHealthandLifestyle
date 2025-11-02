import streamlit as st

st.set_page_config(
    page_title="Objective 1"
)

# Using HTML for styling with a smooth color box
st.markdown(
    """
    <style>
    .title {
        /* Smooth, single background color (Medium Slate Blue) */
        background: #7b68ee; 
        color: #ffffff; /* White text color for contrast */
        padding: 10px;
        border-radius: 5px;
        /* Thick Black Border: 5px wide, solid style, black color */
        border: 5px solid #000000;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5); /* Shadow for depth */
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
