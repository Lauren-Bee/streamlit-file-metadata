{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c4e2eb4-c8c5-4589-8659-471add3c3a42",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import streamlit as st\n",
    "from datetime import datetime\n",
    "\n",
    "# Function to collect file details\n",
    "def collect_file_details(folder_path):\n",
    "    file_data = []\n",
    "    for root, dirs, files in os.walk(folder_path):\n",
    "        for file in files:\n",
    "            file_path = os.path.join(root, file)\n",
    "            file_info = {\n",
    "                \"File Title\": file,\n",
    "                \"Folder Title\": os.path.basename(root),\n",
    "                \"Full Path\": file_path,\n",
    "                \"Created Date\": datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d'),\n",
    "                \"Last Updated Date\": datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d'),\n",
    "                \"Size (KB)\": round(os.path.getsize(file_path) / 1024, 2),\n",
    "            }\n",
    "            file_data.append(file_info)\n",
    "    return file_data\n",
    "\n",
    "# Streamlit app\n",
    "st.title(\"File Metadata Generator\")\n",
    "st.markdown(\"Enter the folder path below to generate metadata for all files in the folder and its subfolders.\")\n",
    "\n",
    "# Input for folder path\n",
    "folder_path = st.text_input(\"Enter Folder Path:\")\n",
    "\n",
    "# Button to generate metadata\n",
    "if st.button(\"Generate Metadata\"):\n",
    "    if os.path.exists(folder_path):\n",
    "        # Collect file details\n",
    "        file_details = collect_file_details(folder_path)\n",
    "        df = pd.DataFrame(file_details)\n",
    "        \n",
    "        # Display the DataFrame in Streamlit\n",
    "        st.write(df)\n",
    "        \n",
    "        # Add current date to output file name\n",
    "        current_date = datetime.now().strftime('%Y-%m-%d')\n",
    "        output_file = f\"file_metadata_{current_date}.xlsx\"\n",
    "        \n",
    "        # Save to Excel\n",
    "        df.to_excel(output_file, index=False)\n",
    "        \n",
    "        # Provide a download button\n",
    "        st.download_button(\n",
    "            label=\"Download Metadata\",\n",
    "            data=open(output_file, 'rb'),\n",
    "            file_name=output_file,\n",
    "            mime=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\",\n",
    "        )\n",
    "    else:\n",
    "        st.error(\"Invalid folder path. Please check and try again.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
