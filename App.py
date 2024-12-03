import streamlit as st
import pandas as pd

# Define the 25 tools and their explanations
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

tool_explanations = {
    "Ad Marketing Platform": "Platforms used for managing and optimizing online advertising campaigns, such as Google Ads or Facebook Ads.",
    "Email Platform": "Tools for managing email communication and campaigns, like Mailchimp or Gmail.",
    "Text/Phone Platform": "Systems for managing text messaging or phone communications, such as Twilio or Google Voice.",
    "Website Platform": "Platforms to build, host, and manage websites, such as WordPress or Wix.",
    "Hosting Platform": "Services that provide hosting for websites or applications, like Bluehost or AWS.",
    "E-commerce Platform": "Platforms for selling products online, such as Shopify or WooCommerce.",
    "Landing Page Platform": "Tools to create high-converting landing pages, like Leadpages or Unbounce.",
    "Messaging Marketing Platform": "Platforms for managing marketing messages via SMS or chat, such as ManyChat or ActiveCampaign.",
    "Payment Platform": "Systems for processing payments, like Stripe, PayPal, or QuickBooks.",
    "Booking Platform": "Tools for scheduling and managing appointments, such as Calendly or Acuity.",
    "Webinar Platform": "Platforms for hosting webinars or virtual events, like Zoom or WebinarJam.",
    "Course Platform": "Tools for creating and selling online courses, such as Teachable or Thinkific.",
    "Podcast Platform": "Systems for recording, editing, and distributing podcasts, like Anchor or Buzzsprout.",
    "CMS/CRM Platform": "Content management and customer relationship management tools, like HubSpot or Salesforce.",
    "Video Host Platform": "Platforms for hosting and sharing videos, such as Vimeo or YouTube.",
    "Storage Platform": "Cloud storage services like Google Drive, Dropbox, or OneDrive.",
    "Document Platform": "Tools for creating and managing documents, such as Google Docs or Microsoft Word.",
    "Automation Platform": "Platforms to automate tasks and workflows, like Zapier or Integromat.",
    "Customer Service Platform": "Tools for managing customer support and interactions, such as Zendesk or Freshdesk.",
    "Tracking & Metrics Platform": "Systems for tracking performance metrics, like Google Analytics or Mixpanel.",
    "Graphic Design Platform": "Tools for creating graphic designs, such as Canva or Adobe Photoshop.",
    "Video Design Platform": "Platforms for video editing and design, like Final Cut Pro or Adobe Premiere.",
    "Copy/Script Design Platform": "Tools for writing and editing scripts or copy, like Grammarly or Jasper.",
    "Separate Engine Platform": "Custom engines or tools tailored for specific needs, such as Algolia for search.",
    "Publishing Platform": "Tools for publishing and distributing content, such as Medium or WordPress.",
}

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ["Form", "Tool Explanations"])

# Form Page
if page == "Form":
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

# Tool Explanations Page
if page == "Tool Explanations":
    st.title("Tool Explanations")
    st.write("Learn more about the purpose and usage of each tool listed in the form.")

    for tool, explanation in tool_explanations.items():
        st.subheader(tool)
        st.write(explanation)

# Footer
st.sidebar.info("Use the sidebar to navigate between the form and explanations.")
