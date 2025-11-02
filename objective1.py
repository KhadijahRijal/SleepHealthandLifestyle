import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Force light theme (no gridlines)
plt.style.use('default')
sns.set_theme(style="white")  # white background, no gridlines

st.set_page_config(
    page_title="Objective 2"
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

st.markdown(
    """
    <div style="
        background-color:#BDB5D5;
        color: #000000; /* Black text color for contrast */;
        padding:15px 20px;
        border-radius:10px;
        border:1px solid #d1d5db;
    ">
   <b>The Visualization is counting population of Gender, Age and Occupation</b>
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


# --- Dynamic Metrics Row (Real values from dataset) ---
st.markdown("### Key Indicators")


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
    # --- DYNAMIC METRICS SECTION (UPDATED) ---
    total_respondents = len(df)
    avg_age = df["Age"].mean()
    male_percent = (df["Gender"].value_counts(normalize=True).get("Male", 0) * 100)
    female_percent = (df["Gender"].value_counts(normalize=True).get("Female", 0) * 100)
    most_common_occupation = df["Occupation"].mode()[0]
    unique_occupations = df["Occupation"].nunique()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Total Respondents", value=total_respondents)
    col2.metric(label="Average Age", value=f"{avg_age:.1f}")
    col3.metric(label="Gender ♂️/♀️", value=f"{male_percent:.1f}% / {female_percent:.1f}%")
    col4.metric(label="Top Job", value=f"{most_common_occupation}")

    
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


# Visualize age distribution by gender
st.subheader("Age Distribution by Gender")

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Gender', multiple='stack', bins=20, kde=True, ax=ax)  # Replace DataFrame with df

ax.set_title('Age Distribution by Gender')
ax.set_xlabel('Age')
ax.set_ylabel('Count')

# Display the plot in Streamlit
st.pyplot(fig)

# Add the main introduction paragraph
st.markdown(
    """
    <div style='text-align: center;'>
        Figure 1
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
    The age distribution of people by gender is seen in this figure 1. 
    The y-axis displays the number of people in each age group, while the x-axis shows age, which ranges from 30 to 60 years. 
    Males are represented by blue bars and a blue density curve, whereas females are represented by orange bars and an orange curve.
    </div>
    """,
    unsafe_allow_html=True
)


# Visualize the distribution of the 'Age' column
st.subheader("Distribution of Age")

fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data=df, x='Age', bins=20, kde=False, ax=ax)  # replace DataFrame with df

ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Age')

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
   The total distribution of age in the dataset is displayed in this graph. 
   Age from 30 to 60 is represented by the x-axis, while the frequency of people in each age group is displayed on the y-axis.
    </div>
    """,
    unsafe_allow_html=True
)


# Get the value counts for the 'Occupation' column
occupation_counts = df['Occupation'].value_counts()  # Replace DataFrame with df

# Streamlit title
st.subheader("Distribution of Occupation")

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    occupation_counts,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=1.1
)

# Add a legend to display the occupation labels
ax.legend(
    wedges,
    occupation_counts.index,
    title="Occupation",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

ax.set_title('Distribution of Occupation')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Display the plot in Streamlit
st.pyplot(fig)

# Add the main introduction paragraph
st.markdown(
    """
    <div style='text-align: center;'>
        Figure 3
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
    The distribution of occupations within a dataset is displayed in this pie chart.
    Each slice, which is labelled with its fraction of the total, represents a different occupational type.
    </div>
    """,
    unsafe_allow_html=True
)
