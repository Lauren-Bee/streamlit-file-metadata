import os
import pandas as pd
import streamlit as st
from datetime import datetime

# Function to collect file details
def collect_file_details(folder_path):
    file_data = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_info = {
                "File Title": file,
                "Folder Title": os.path.basename(root),
                "Full Path": file_path,
                "Created Date": datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d'),
                "Last Updated Date": datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d'),
                "Size (KB)": round(os.path.getsize(file_path) / 1024, 2),
            }
            file_data.append(file_info)
    return file_data

# Streamlit app
st.title("File Metadata Generator")
st.markdown("Enter the folder path below to generate metadata for all files in the folder and its subfolders.")

# Input for folder path
folder_path = st.text_input("Enter Folder Path:")

# Debug: Display the entered folder path
st.write(f"Entered folder path: {folder_path}")

# Button to generate metadata
if st.button("Generate Metadata"):
    if os.path.exists(folder_path):
        # Collect file details
        file_details = collect_file_details(folder_path)
        df = pd.DataFrame(file_details)
        
        # Display the DataFrame in Streamlit
        st.write(df)
        
        # Add current date to output file name
        current_date = datetime.now().strftime('%Y-%m-%d')
        output_file = f"file_metadata_{current_date}.xlsx"
        
        # Save to Excel
        df.to_excel(output_file, index=False)
        
        # Provide a download button
        st.download_button(
            label="Download Metadata",
            data=open(output_file, 'rb'),
            file_name=output_file,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    else:
        st.error("Invalid folder path. Please check and try again.")
