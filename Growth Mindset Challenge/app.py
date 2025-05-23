import streamlit as st
import pandas as pd
import os
from io import BytesIO


st.set_page_config(page_title= "💿Data_Sweeper", layout = "wide")
st.title("💿Data_Sweeper")
st.write("Transform your files between CSV and EXCEl formats with built-in data cleaning and visualization")
uploaded_files=st.file_uploader("Upload your files(CSV or Excel):", type=["csv","xlsx"],accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext=os.path.splitext(file.name)[-1].lower()

        if file_ext==".csv":
            df=pd.read_csv(file)

        elif file_ext==".xlsx":
            df=pd.read_excel(file)
        
        else:
            st.error(f"Unsupported File Type : {file_ext}")
            continue

        st.write(f"**File Name**: {file.name} ")
        file_size_kb=round(file.getbuffer().nbytes/1024 , 2)
        st.write(f"**File Size** : {file_size_kb} KBs")
        
        st.write("**Preview the head of the Dataframe**")
        st.dataframe(df.head())

        st.subheader("Data Cleaning Options")
        
        if st.checkbox(f"Clean Data for {file.name}"):
            col1,col2=st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates From {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicate Removed!")
            
            
            with col2:
                if st.button(f"Fill Missing Values For {file.name}"):
                    numeric_cols=df.select_dtypes(include=["number"]).columns
                    df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values Have Been Filled!")
            
        st.subheader("Select Columns to Convert")
        column_list = list(df.columns)

        columns = st.multiselect(f"Choose Columns for {file.name}", column_list, default=column_list)

        if columns:
            df = df[columns]
        else:
            st.warning("⚠️ Please select at least one column!")

        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])

        st.subheader("Conversion Options")
        conversion_type=st.radio(f"Convert {file.name} to:", ["CSV","Excel"],key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer=BytesIO()
            if conversion_type=="CSV":
                df.to_csv(buffer,index=False)
                file_name=file.name.replace(file_ext,".csv")
                mime_type="text/csv"
            if conversion_type=="Excel":
                df.to_excel(buffer,index=False)
                file_name=file.name.replace(file_ext,".xlsx")
                mime_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

            st.success("🎉 All files processed successfully!") 



