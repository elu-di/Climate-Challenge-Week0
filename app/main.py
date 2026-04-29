import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title("African Climate Comparison Dashboard")
st.write("Interactive dashboard for comparing climate trends across countries.")

# Load data
DATA_PATH = Path("data")
files = list(DATA_PATH.glob("*_clean.csv"))

@st.cache_data
def load_data():
    frames = []
    for file in files:
        df = pd.read_csv(file)
        country = file.stem.replace("_clean", "").capitalize()
        df["Country"] = country
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"])
            df["Year"] = df["Date"].dt.year
        frames.append(df)
    return pd.concat(frames, ignore_index=True)

if not files:
    st.warning("No cleaned CSV files found in data/ folder.")
    st.stop()

df = load_data()

# Sidebar controls
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select countries",
    options=sorted(df["Country"].unique()),
    default=sorted(df["Country"].unique())
)

min_year = int(df["Year"].min())
max_year = int(df["Year"].max())
selected_years = st.sidebar.slider(
    "Select year range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

variable = st.sidebar.selectbox(
    "Select variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

# Filter data
filtered_df = df[
    (df["Country"].isin(selected_countries)) &
    (df["Year"] >= selected_years[0]) &
    (df["Year"] <= selected_years[1])
]

# Temperature trend line chart
st.subheader("Temperature Trend")
trend = filtered_df.groupby(["Year", "Country"])["T2M"].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
for country in trend["Country"].unique():
    country_data = trend[trend["Country"] == country]
    ax.plot(country_data["Year"], country_data["T2M"], label=country)
ax.set_xlabel("Year")
ax.set_ylabel("Average Temperature (T2M)")
ax.legend()
st.pyplot(fig)

# Variable distribution boxplot
st.subheader(f"{variable} Distribution")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_df, x="Country", y=variable, ax=ax)
st.pyplot(fig)

# Data preview
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head())

st.markdown("### Usage Instructions")
st.markdown("- Select one or more countries from the sidebar.\n- Adjust the year range to zoom into a period.\n- Choose a variable to compare distributions.")

