import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Force light theme (no gridlines)
plt.style.use('default')
sns.set_theme(style="white")  # white background, no gridlines

st.set_page_config(
    page_title="Objective 3"
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
        <h1>Objective 3</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        background-color:#BDB5D5;
        color: #000000; /* Black text color for contrast */;
        padding:15px 20px;
        border-radius:10px;
        border:1px solid #d1d5db;
    ">
    <b>Scientific Visualization</b> is a multidisciplinary field that focuses on transforming complex
    scientific data into visual forms that are easier to understand, interpret, and communicate.
    Through the use of computational techniques, visualization helps researchers explore datasets,
    identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
    </div>
    """,
    unsafe_allow_html=True
)

# --- Configuration for Dark Mode / Purple Theme ---
# Note: Streamlit theming is best done via .streamlit/config.toml, 
# but we can set up the page layout here and use markdown for color accents.
# Custom CSS for the Purple/Black theme
# This targets the main title and applies a purple accent.
st.markdown("""
<style>
    /* Main Header Styling */
    .stApp {
        background-color: #1a1a1a; /* Dark background */
        color: #e0e0e0; /* Light text for contrast */
    }
    h1 {
        color: #8A2BE2; /* Primary Purple for main title */
        font-weight: 700;
        text-shadow: 2px 2px 4px #000000;
    }
    h2 {
        color: #BA55D3; /* Medium Purple for headers */
        border-bottom: 2px solid #8A2BE2;
        padding-bottom: 5px;
    }
    /* Ensure text in main sections is light */
    .st-emotion-cache-nahz7x, 
    .st-emotion-cache-163l4a8, 
    .st-emotion-cache-12fm5so {
        color: #e0e0e0 !important;
    }
</style>
""", unsafe_allow_html=True)


# --- Data Loading and Caching ---
DATA_URL = "https://raw.githubusercontent.com/KhadijahRijal/SleepHealthandLifestyle/refs/heads/main/cleaned_sleep_health_data.csv"

@st.cache_data
def load_data(url):
    """Loads and returns the DataFrame from the specified URL."""
    try:
        data = pd.read_csv(url)
        # Drop any unnamed columns that might result from CSV indexing
        data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data(DATA_URL)


# --- Dashboard Layout ---

st.title("💜 Sleep Health and Lifestyle Dataset")

if df.empty:
    st.warning("Could not load the dataset. Please check the URL and internet connection.")
else:
    # --- Pandas Styler Definition for Purple/Black Theme ---
    # Define styles for table (header and alternating rows)
    table_styles = [
        # Header style (Dark Purple Accent)
        {'selector': 'thead th',
         'props': [('background-color', '#3c1b50'), ('color', '#e0e0e0'), ('font-weight', 'bold')]},
        # Even rows (Dark Gray/Black)
        {'selector': 'tbody tr:nth-child(even)',
         'props': [('background-color', '#2c2c2c'), ('color', '#e0e0e0')]},
        # Odd rows (Slightly Lighter Dark Gray)
        {'selector': 'tbody tr:nth-child(odd)',
         'props': [('background-color', '#3a3a3a'), ('color', '#e0e0e0')]},
    ]
    
    # 1. Full Dataset Display
    st.header("Dataset")
    st.write(f"The dataset contains **{len(df)}** rows and **{len(df.columns)}** columns.")
    
    # Apply styling to the full DataFrame
    styled_df = df.style.set_table_styles(table_styles)
    st.dataframe(styled_df, use_container_width=True)

    # 2. Summary Statistics Display
    st.header("Summary Statistics")
    st.write("Descriptive statistics for all numerical columns in the dataset.")

    # Calculate the summary DataFrame
    summary_df = df.describe(include=np.number).transpose()
    
    # Format the summary and apply the table styles
    styled_summary_df = summary_df.style.format("{:,.2f}").set_table_styles(table_styles)

    # Display the summary DataFrame
    st.dataframe(styled_summary_df, use_container_width=True)

    # 3. Data Dictionary / Info (Using a basic info section)
    st.header("Data Column Information")
    st.write("Below is a quick look at the column names and their data types.")
    
    info_data = []
    for col, dtype in df.dtypes.items():
        info_data.append({
            'Column Name': col,
            'Data Type': str(dtype),
            'Non-Null Count': df[col].count()
        })
    
    info_df = pd.DataFrame(info_data)
    
    # Apply styling to the info DataFrame
    styled_info_df = info_df.style.set_table_styles(table_styles)
    st.dataframe(styled_info_df, use_container_width=True)

# Footer for running the app
st.markdown("""
---
*To run this application, save the code as `sleep_data_dashboard.py` and execute:*
`streamlit run sleep_data_dashboard.py`
""", unsafe_allow_html=True)

st.write("Available columns:", list(df.columns))

# Clean column names (strip spaces, make lowercase)
df.columns = df.columns.str.strip().str.lower()

# Then use lowercase names
expected_cols = ['quality of sleep', 'systolic', 'diastolic']
available_cols = [col for col in expected_cols if col in df.columns]

if len(available_cols) < 3:
    st.error(f"Missing columns! Found only: {available_cols}")
else:
    correlation_data = df[available_cols]
    correlation_matrix = correlation_data.corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title("Correlation Matrix of Quality of Sleep and Blood Pressure")
    st.pyplot(fig)



# Streamlit section title
st.subheader("Correlation Matrix of Quality of Sleep and Blood Pressure")

# Select the relevant numerical columns
correlation_data = df[['Quality of Sleep', 'Blood Pressure (Systolic)', 'Blood Pressure (Diastolic)']]  # Replace DataFrame with df

# Calculate the correlation matrix
correlation_matrix = correlation_data.corr()

# Create the heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title("Correlation Matrix of Quality of Sleep and Blood Pressure")

# Display the heatmap in Streamlit
st.pyplot(fig)

# Add the main introduction paragraph
st.markdown(
    """
    <div style='text-align: center;'>
        Figure 2
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="
        background-color:#BDB5D5;
        color: #000000; /* Black text color for contrast */;
        padding:15px 20px;
        border-radius:10px;
        border:1px solid #d1d5db;
    ">
    is a multidisciplinary field that focuses on transforming complex
    scientific data into visual forms that are easier to understand, interpret, and communicate.
    Through the use of computational techniques, visualization helps researchers explore datasets,
    identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
    </div>
    """,
    unsafe_allow_html=True
)


# Streamlit section title
st.subheader("Sleep Duration Distribution by Sleep Disorder")

# Create a violin plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.violinplot(x='Sleep Disorder', y='Sleep Duration', data=df, ax=ax)  # Replace DataFrame with df
ax.set_title('Sleep Duration Distribution by Sleep Disorder')
ax.set_xlabel('Sleep Disorder')
ax.set_ylabel('Sleep Duration')

# Display the plot in Streamlit
st.pyplot(fig)

# Add the main introduction paragraph
st.markdown(
    """
    <div style='text-align: center;'>
        Figure 2
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="
        background-color:#BDB5D5;
        color: #000000; /* Black text color for contrast */;
        padding:15px 20px;
        border-radius:10px;
        border:1px solid #d1d5db;
    ">
    is a multidisciplinary field that focuses on transforming complex
    scientific data into visual forms that are easier to understand, interpret, and communicate.
    Through the use of computational techniques, visualization helps researchers explore datasets,
    identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
    </div>
    """,
    unsafe_allow_html=True
)


# Streamlit section title
st.subheader("Physical Activity Level Distribution by BMI Category")

# Create a box plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='BMI Category', y='Physical Activity Level', data=df, ax=ax)  # Replace DataFrame with df
ax.set_title('Physical Activity Level Distribution by BMI Category')
ax.set_xlabel('BMI Category')
ax.set_ylabel('Physical Activity Level')

# Display the plot in Streamlit
st.pyplot(fig)

# Add the main introduction paragraph
st.markdown(
    """
    <div style='text-align: center;'>
        Figure 2
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="
        background-color:#BDB5D5;
        color: #000000; /* Black text color for contrast */;
        padding:15px 20px;
        border-radius:10px;
        border:1px solid #d1d5db;
    ">
    is a multidisciplinary field that focuses on transforming complex
    scientific data into visual forms that are easier to understand, interpret, and communicate.
    Through the use of computational techniques, visualization helps researchers explore datasets,
    identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
    </div>
    """,
    unsafe_allow_html=True
)
