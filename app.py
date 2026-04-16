import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- CONFIGURATION ---
# Apni API key dhyan se check karein (Quotes ke andar)
API_KEY = "AQ.Ab8RN6IwqAqM9Q-m6QXpji0EiQi9_EXIZCrvyLeP7HC4ee-4KQ" 

# AI Setup - Latest version configuration
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Cleardeals Automation", layout="wide")
st.title("🏠 Cleardeals Property Data Extractor")

raw_text = st.text_area("Paste WhatsApp Messages here:", height=300)

if st.button("Generate CSV"):
    if not raw_text:
        st.warning("Pehle data paste karein!")
    else:
        with st.spinner("AI processing kar raha hai..."):
            try:
                # Humne model ka naam 'gemini-1.5-flash' se 'gemini-pro' ya latest rakha hai
                model = genai.GenerativeModel('gemini-pro') 
                
                prompt = f"Extract property data from this text into a CSV table. Columns: Date, Category, Property Code, Owner Name, Owner Contact, BHK, Area, Locality, Project Name, Floor, Furnishing (Strictly: Furnished, Semi-Furnished, or Unfurnished), Price, Deposit, Source. If data is missing, use 'N/A'. Text: {raw_text}"
                
                response = model.generate_content(prompt)
                
                # CSV Data extraction
                csv_data = response.text.replace('```csv', '').replace('```', '').strip()
                
                if csv_data:
                    st.success("Data ready hai!")
                    st.download_button(label="📥 Download CSV File", data=csv_data, file_name="properties.csv", mime="text/csv")
                else:
                    st.error("AI data extract nahi kar paaya. Dubara try karein.")
            except Exception as e:
                st.error(f"Error detail: {e}")
