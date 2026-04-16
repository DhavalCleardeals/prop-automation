import streamlit as st
import pandas as pd
import google.generativeai as genai

# Tijori (Secrets) se chabi nikalna
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
else:
    st.error("Secrets mein API Key nahi mili! Settings > Secrets mein check karein.")
    st.stop()

st.set_page_config(page_title="Cleardeals Automation", layout="wide")
st.title("🏠 Cleardeals Property Data Extractor")

raw_text = st.text_area("WhatsApp Message Paste Karein:", height=300)

if st.button("Generate CSV"):
    if not raw_text:
        st.warning("Pehle data paste karein!")
    else:
        with st.spinner("AI processing kar raha hai..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Extract property data into a CSV table. Columns: Date, Category, Property Code, Owner Name, Owner Contact, BHK, Area, Locality, Project Name, Floor, Furnishing (Strictly: Furnished, Semi-Furnished, Unfurnished), Price, Deposit, Source. Data: {raw_text}"
                response = model.generate_content(prompt)
                csv_data = response.text.replace('```csv', '').replace('```', '').strip()
                st.success("Data taiyar hai!")
                st.download_button("📥 Download CSV", csv_data, "properties.csv", "text/csv")
            except Exception as e:
                st.error(f"Error: {e}")
