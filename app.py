import streamlit as st
import pdfplumber

# Function to read PDF
def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n\n"
    return text

# Define sections with keywords
sections = {
    "Property Info": "Appraisal Of Real Property",
    "Neighborhood Analysis": "Neighborhood",
    "Site & Improvements": "Improvements",
    "Comparables": "Comparable",
    "Cost Approach": "COST APPROACH",
    "Market Conditions": "Market Conditions",
    "Certification": "APPRAISER'S CERTIFICATION"
}

# Streamlit UI
st.title("📑 PDF Appraisal Report Viewer:")

uploaded_file = st.file_uploader("Upload your Appraisal PDF", type=["pdf"])

if uploaded_file:
    pdf_text = read_pdf(uploaded_file)

    st.sidebar.header("📌 Choose Sections")
    selected_sections = []

    for section in sections:
        if st.sidebar.checkbox(section, value=False):
            selected_sections.append(section)

    if not selected_sections:
        st.subheader("Full Report")
        st.text(pdf_text)
    else:
        for section in selected_sections:
            st.subheader(section)
            keyword = sections[section]
            start = pdf_text.find(keyword)
            if start != -1:
                st.text(pdf_text[start:start+2500])  # show snippet
            else:
                st.text("⚠️ Section not found in this document.")
