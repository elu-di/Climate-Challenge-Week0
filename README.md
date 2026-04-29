# Climate Challenge Week 0 - African Climate Comparison

## Project Overview
This project is an interactive climate dashboard that allows users to compare climate trends across multiple African countries (e.g., Ethiopia, Tanzania, Nigeria). It is built using Python, Pandas, Matplotlib, Seaborn, and Streamlit. 

The goal of this dashboard is to provide clear visualizations of temperature trends and the distribution of various climate variables over time.

## Features
- **Interactive Filtering**: Users can filter data by specific countries and define custom year ranges using a sidebar.
- **Temperature Trends**: Visualizes the average temperature (`T2M`) over the years for selected countries using a line chart.
- **Variable Distribution**: Displays the distribution of selected variables (like `T2M`, `PRECTOTCORR`, `RH2M`) using boxplots to easily compare across countries.
- **Data Preview**: Shows a tabular view of the filtered dataset.

## Project Structure
- `app/`: Contains the Streamlit web application (`main.py`).
- `data/`: Contains the climate data in CSV format (e.g., `ethiopia.csv`, `tanzania.csv`, `nigeria.csv`).
- `notebooks/`: Contains Jupyter notebooks (`compare_countries.ipynb`) used for exploratory data analysis (EDA) and cleaning.
- `requirements.txt`: Lists the Python dependencies required to run the project.

## How to Run the Dashboard

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Climate-Challenge-Week0
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application:**
   ```bash
   python -m streamlit run app/main.py
   ```
   This will start a local server and open the dashboard in your default web browser.

## Contributions and Implementation
- Cleaned and preprocessed raw climate datasets for three different countries.
- Conducted exploratory data analysis using Jupyter Notebooks to understand trends.
- Developed a modular Streamlit application to visualize and interact with the data dynamically.
