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
        <h1>Objective 2</h1>
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
    <b>The graph illustrates comparison between Gender, Age, Occupation with theirs Quality of Sleep.</b>
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
    
    # --- DYNAMIC METRICS SECTION ---
    total_respondents = mean(df)
    avg_age = df["Age"].mean()
    male_percent = (df["Gender"].value_counts(normalize=True).get("Male", 0) * 100)
    female_percent = (df["Gender"].value_counts(normalize=True).get("Female", 0) * 100)
    most_common_occupation = df["Occupation"].mode()[0]
    unique_occupations = df["Occupation"].nunique()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric(label="Total Respondents", value=total_respondents)
    col2.metric(label="Average Age", value=f"{avg_age:.1f}")
    col3.metric(label="Gender (Male)", value=f"{male_percent:.1f}%")
    col4.metric(label="Gender (Female)", value=f"{female_percent:.1f}%")
    col5.metric(label="Top Job", value=f"{most_common_occupation}")
    
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


# Streamlit section title
st.subheader("Average Quality of Sleep by Gender")

# Create the bar plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='Gender', y='Quality of Sleep', data=df, ax=ax)  # Replace DataFrame with df
ax.set_title('Average Quality of Sleep by Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Quality of Sleep')

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
   The average sleep quality for male and female is compared in this bar graph.
   The average sleep quality score is displayed on the y-axis, while gender is represented on the x-axis.
    </div>
    """,
    unsafe_allow_html=True
)


# Streamlit section title
st.subheader("Distribution of Quality of Sleep by Age Group")

# Create age bins
age_bins = [20, 30, 40, 50, 60]
age_labels = ['20-29', '30-39', '40-49', '50-59']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)  # Replace DataFrame with df

# Create a cross-tabulation of Age Group and Quality of Sleep
quality_by_age = pd.crosstab(df['Age_Group'], df['Quality of Sleep'])

# Create a stacked bar plot
fig, ax = plt.subplots(figsize=(10, 7))
quality_by_age.plot(kind='bar', stacked=True, ax=ax, colormap='viridis')

ax.set_title('Distribution of Quality of Sleep by Age Group')
ax.set_xlabel('Age Group')
ax.set_ylabel('Count')
ax.legend(title='Quality of Sleep')
plt.xticks(rotation=45)
plt.tight_layout()

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
    The distribution of sleep quality between different ages is displayed in this bar graph.
    People are divided into four age categories on the x-axis which is, 20–29, 30–39, 40–49, and 50–59. 
    The number of people in each category is shown on the y-axis.
    </div>
    """,
    unsafe_allow_html=True
)


# Streamlit section title
st.subheader("Average Quality of Sleep by Occupation (Line Chart)")

# Calculate the average Quality of Sleep for each Occupation and sort by Occupation
occupation_quality_mean = (
    df.groupby('Occupation')['Quality of Sleep']
    .mean()
    .reset_index()
    .sort_values(by='Occupation')
)  # Replace DataFrame with df

# Create a line chart
fig, ax = plt.subplots(figsize=(12, 8))
sns.lineplot(x='Occupation', y='Quality of Sleep', data=occupation_quality_mean, marker='o', ax=ax)

ax.set_title('Average Quality of Sleep by Occupation (Line Chart)')
ax.set_xlabel('Occupation')
ax.set_ylabel('Average Quality of Sleep')
ax.grid(True)
plt.xticks(rotation=90)

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
    The average sleep quality for different occupations is displayed in this line graph.
    The y-axis, which ranges from 4.0 to 8.0, represents average sleep quality, while the x-axis displays different occupations.
    </div>
    """,
    unsafe_allow_html=True
)
