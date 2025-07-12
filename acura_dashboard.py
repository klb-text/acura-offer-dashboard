import streamlit as st
import pandas as pd

st.set_page_config(page_title="Acura Lease & APR Offer Comparison", layout="wide")

st.title("🚗 Acura Lease & APR Offer Comparison Dashboard")

# Upload lease and APR files
lease_file = st.file_uploader("Upload Lease Offer File", type=["csv", "xlsx"])
apr_file = st.file_uploader("Upload APR Offer File", type=["csv", "xlsx"])
mapping_file = st.file_uploader("Upload Mapping File (optional)", type=["csv", "xlsx"])

def load_file(file):
    if file is not None:
        if file.name.endswith(".csv"):
            return pd.read_csv(file)
        else:
            return pd.read_excel(file)
    return None

lease_df = load_file(lease_file)
apr_df = load_file(apr_file)
map_df = load_file(mapping_file)

# Display uploaded data
if lease_df is not None:
    st.subheader("Lease Offers")
    st.dataframe(lease_df)

if apr_df is not None:
    st.subheader("APR Offers")
    st.dataframe(apr_df)

if map_df is not None:
    st.subheader("Mapping File")
    st.dataframe(map_df)

# Placeholder for future comparison logic
if lease_df is not None and apr_df is not None:
    st.success("Both Lease and APR files uploaded. Ready for comparison logic!")

