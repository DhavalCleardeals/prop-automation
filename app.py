import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- CONFIGURATION ---
# Yahan apni NAYI key dhyan se paste karein
API_KEY = "YAHAN_NAYI_KEY_PASTE_KAREIN" 

if API_KEY != "AQ.Ab8RN6KNQHfvUKCe6fF5gPDQ0gzkNv3u11GaBIWw5B3x9O7jug":
    genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Cleardeals Automation", layout="wide")
st.title("🏠 Cleardeals Property Data Extractor")

raw_text = st.text_area("Paste WhatsApp Messages here:", height=300)

if st.button("Generate CSV"):
    if not raw_text:
        st.warning("Pehle data paste karein!")
    elif API_KEY == "YAHAN_NAYI_KEY_PASTE_KAREIN":
        st.error("API Key missing hai! Code mein apni key dalein.")
    else:
        with st.spinner("AI processing kar raha hai..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Extract property data from this text into a CSV table. Columns: Date, Category, Property Code, Owner Name, Owner Contact, BHK, Area, Locality, Project Name, Floor, Furnishing (Strictly use: Furnished, Semi-Furnished, or Unfurnished), Price, Deposit, Source. If data is missing, use 'N/A'. Text: {raw_text}"
                
                response = model.generate_content(prompt)
                csv_data = response.text.replace('```csv', '').replace('```', '').strip()
                
                st.success("Data ready hai!")
                st.download_button(label="📥 Download CSV File", data=csv_data, file_name="properties.csv", mime="text/csv")
            except Exception as e:
                st.error(f"Error detail: {e}")
