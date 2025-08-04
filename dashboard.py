import streamlit as st
import pandas as pd
import os
import sqlite3
from PIL import Image

st.set_page_config(page_title="Inventory Dashboard", layout="wide")

conn = sqlite3.connect("inventory.db")
df = pd.read_sql_query("SELECT * FROM inventory", conn)

st.markdown("## 📦 Voice-Controlled Inventory Dashboard")

st.sidebar.header("🔍 Filters")
search_item = st.sidebar.text_input("Search by Item Name")
search_location = st.sidebar.text_input("Search by Location")
show_qr = st.sidebar.checkbox("Show QR Code Preview")

filtered_df = df.copy()
if search_item:
    filtered_df = filtered_df[filtered_df["item"].str.contains(search_item, case=False)]
if search_location:
    filtered_df = filtered_df[filtered_df["location"].str.contains(search_location, case=False)]

st.markdown("### 🗂️ Inventory Records (" + str(len(filtered_df)) + ")")
st.dataframe(filtered_df[["id", "item", "quantity", "location", "timestamp"]])

if show_qr:
    st.markdown("### 📚 QR Codes Archive")
    for _, row in filtered_df.iterrows():
        qr_label = f"{row['item']} ({row['quantity']}) @ {row['location']} on {row['timestamp']}"
        st.markdown(f"**{qr_label}**")
        try:
            image = Image.open(row["qr_path"])
            st.image(image, width=200)
        except Exception as e:
            st.warning(f"Unable to load QR image for {row['item']}: {e}")

st.download_button(
    label="📥 Download Inventory as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="inventory_records.csv",
    mime="text/csv",
)