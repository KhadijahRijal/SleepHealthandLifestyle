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
          Original: background: linear-gradient(90deg, #ff69b4, #8a2be2, #00bfff);
          Lighter:  Using lighter shades, e.g.,
          #ff8fab (Light Pink) -> #a992f0 (Light Purple/Lavender) -> #66d9ff (Light Blue/Cyan)
        */
        background: linear-gradient(90deg, #ff8fab, #a992f0, #66d9ff); /* Lighter Gradient */
        color: #000000; /* Changed to black text for better contrast on a lighter background */
        padding: 10px;
        border-radius: 5px;
        border: 2px solid transparent;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3); /* Slightly softer shadow */
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
