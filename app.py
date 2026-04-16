import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- CONFIGURATION ---
# Yahan apni AQ... wali key paste karein
API_KEY = AQ.Ab8RN6Il8h3nnt3zhtObEL-XIun-Tm9m-zAuGXRwTDWZEC3Yiw 
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Cleardeals Automation", layout="wide")
st.title("🏠 Cleardeals Property Data Extractor")
st.write("WhatsApp data paste karein aur CSV download karein.")

raw_text = st.text_area("Paste WhatsApp Messages here:", height=300)

if st.button("Generate CSV"):
    if not raw_text:
        st.warning("Pehle data paste karein!")
    else:
        with st.spinner("AI processing kar raha hai..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Extract property data from this text into a CSV table. Columns: Date, Category, Property Code, Owner Name, Owner Contact, BHK, Area, Locality, Project Name, Floor, Furnishing (Strictly: Furnished, Semi-Furnished, Unfurnished), Price, Deposit, Source. If data is missing, use 'N/A'. Text: {raw_text}"
            
            response = model.generate_content(prompt)
            # Safely cleaning the AI response to get only CSV data
            csv_data = response.text.replace('```csv', '').replace('```', '').strip()
            
            st.success("Data ready hai!")
            st.download_button(label="📥 Download CSV File", data=csv_data, file_name="properties.csv", mime="text/csv")
