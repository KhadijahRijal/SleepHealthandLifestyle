import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Objective 1"
)

# Using HTML for styling with a smooth color box
st.markdown(
    """
    <style>
    .title {
        /* Smooth, single background color (Lavender) */
        background: #E6E6FA; 
        color: #000000; /* Black text color for contrast */
        padding: 10px;
        border-radius: 5px;
        /* Thick Black Border: 10px wide, solid style, black color */
        border: 10px solid #000000;
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


st.set_page_config(
    page_title="Objective 1 - Purple & Black Theme",
    layout="wide" # Use wide layout for better display
)

# 1. Define the URL for the CSV data
DATA_URL = "https://raw.githubusercontent.com/KhadijahRijal/SleepHealthandLifestyle/refs/heads/main/cleaned_sleep_health_data.csv"

# 2. Use a cache decorator for efficient data loading
@st.cache_data
def load_data():
    """Loads the CSV data from the URL using pandas."""
    try:
        data = pd.read_csv(DATA_URL)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame() # Return empty DataFrame on failure

# 3. Apply Purple & Black Styling to the Title Box
st.markdown(
    """
    <style>
    /* Custom Title Box Styling: Purple background, thick black border */
    .purple-title-box {
        background: #4B0082; /* Deep Indigo/Purple */
        color: #FFFFFF; /* White text for contrast */
        padding: 15px;
        border-radius: 8px;
        border: 4px solid #000000; /* Thick Black Border */
        text-align: center;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.6); /* Stronger shadow */
    }
    h1 {
        margin: 0;
        font-size: 2.5em;
    }
    </style>
    <div class="purple-title-box">
        <h1>Sleep Health and Lifestyle Data 🌙</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---") # Separator

# 4. Load the data
df = load_data()

# 5. Display the data with potential custom styling (optional)
if not df.empty:
    st.header("Loaded Dataset")
    st.write(f"The dataset contains **{df.shape[0]} rows** and **{df.shape[1]} columns**.")
    
    # You can apply conditional styling to the dataframe using pandas' Styler
    styled_df = df.head(10).style.set_properties(**{'background-color': '#f0eaff',
                                                    'color': '#191970',
                                                    'border-color': '#4B0082'})

    st.dataframe(styled_df, use_container_width=True)
    
    # Display the full DataFrame
    st.dataframe(df, use_container_width=True)

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())
else:
    st.error("Could not load data from the specified URL.")
