import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Acura Lease & APR Offer Comparison", layout="wide")

# Title
st.title("Acura Lease & APR Offer Comparison Dashboard")

# Sidebar for file uploads
st.sidebar.header("Upload Mapping Files")
lease_file = st.sidebar.file_uploader("Upload Lease Mapping File", type=["csv", "xlsx"])
apr_file = st.sidebar.file_uploader("Upload APR Mapping File", type=["csv", "xlsx"])

# Function to read uploaded file
def load_file(uploaded_file):
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            return pd.read_excel(uploaded_file, engine='openpyxl')
    return None

# Load data
lease_data = load_file(lease_file)
apr_data = load_file(apr_file)

# Tabs for Lease and APR views
tab1, tab2 = st.tabs(["Lease Offers", "APR Offers"])

with tab1:
    st.subheader("Lease Offer Mapping")
    if lease_data is not None:
        st.dataframe(lease_data)
        st.info("Matched and unmatched lease offers will be displayed here.")
    else:
        st.warning("Please upload a Lease Mapping File.")

with tab2:
    st.subheader("APR Offer Mapping")
    if apr_data is not None:
        st.dataframe(apr_data)
        st.info("Matched and unmatched APR offers will be displayed here.")
    else:
        st.warning("Please upload an APR Mapping File.")

