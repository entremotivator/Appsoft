import streamlit as st
import pandas as pd

# Define the 25 tools
tools = [
    "Ad Marketing Platform",
    "Email Platform",
    "Text/Phone Platform",
    "Website Platform",
    "Hosting Platform",
    "E-commerce Platform",
    "Landing Page Platform",
    "Messaging Marketing Platform",
    "Payment Platform",
    "Booking Platform",
    "Webinar Platform",
    "Course Platform",
    "Podcast Platform",
    "CMS/CRM Platform",
    "Video Host Platform",
    "Storage Platform",
    "Document Platform",
    "Automation Platform",
    "Customer Service Platform",
    "Tracking & Metrics Platform",
    "Graphic Design Platform",
    "Video Design Platform",
    "Copy/Script Design Platform",
    "Separate Engine Platform",
    "Publishing Platform",
]

# App Header
st.title("Tool Platform Form")
st.write("Fill out the form below with platform names and passwords. Download the completed form as a CSV file.")

# Create the form
with st.form("platform_form"):
    platform_data = {}
    for tool in tools:
        col1, col2 = st.columns(2)
        platform_name = col1.text_input(f"{tool} Name", key=f"{tool}_name")
        password = col2.text_input(f"{tool} Password", key=f"{tool}_password", type="password")
        platform_data[tool] = {"Platform Name": platform_name, "Password": password}
    
    # Submit button
    submitted = st.form_submit_button("Submit")

# Handle form submission
if submitted:
    # Convert form data to a DataFrame
    df = pd.DataFrame.from_dict(platform_data, orient="index")
    
    # Downloadable CSV
    csv = df.to_csv(index=True)
    st.success("Form submitted successfully!")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="platform_form.csv",
        mime="text/csv",
    )
