import streamlit as st

st.set_page_config(
    page_title="Objective 1"
)

# Using HTML for styling with a gradient box
st.markdown(
    """
    <style>
    .title {
        /* Gradient from bright pink to deep purple */
        background: linear-gradient(90deg, #ff1493, #6a059c);
        color: #ffffff; /* White text color for contrast */
        padding: 10px;
        border-radius: 5px;
        /* Custom Border: 3px wide, solid style, black color */
        border: 3px solid #000000;
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
    """,
    unsafe_allow_html=True
)
