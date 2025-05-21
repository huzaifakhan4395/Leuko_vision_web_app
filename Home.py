import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="LeukoVision - Home",
    page_icon="🔬",
    layout="centered"
)

# Custom CSS for a modern clean layout
st.markdown("""
    <style>
        /* Hide sidebar and its toggle button */
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
        /* Hide footer & hamburger menu */
        #MainMenu, footer {
            visibility: hidden;
        }

        /* General page styling */
        .main {
            background-color: #f5f9ff;
            padding-top: 2rem;
        }

        .hero {
            text-align: center;
            padding: 4rem 1rem;
        }

        .hero h1 {
            font-size: 3rem;
            color: #2a2a2a;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.25rem;
            color: #444;
            max-width: 900px;
            margin: auto;
            line-height: 1.6;
        }

        .btn-container {
            text-align: center;
            margin-top: 2.5rem;
        }

        .stButton>button {
            background-color: #8a00c2;
            color: white;
            padding: 0.9rem 2.2rem;
            font-size: 1.1rem;
            border-radius: 10px;
            border: none;
            transition: background-color 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #8a00c2;
        }
    </style>
""", unsafe_allow_html=True)

# # # Optional: Add a logo or healthcare image
# # image = Image.open("Leuko Vision Web App/Images/Leukovision logo.png") if "Leuko Vision Web App/Images/Leukovision logo.png" in os.listdir() else None
# # if image:
# #     st.image(image, width=120)

# logo_path = "Leuko Vision Web App/ChatGPT Image May 21, 2025, 05_43_20 PM.png"  # or "assets/logo.png" if stored in a folder
# if os.path.exists(logo_path):
#     image = Image.open(logo_path)
#     st.image(image, width=200)

# Hero section
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown("### Welcome to")
st.markdown("<h1>🔬LeukoVision</h1>", unsafe_allow_html=True)
st.markdown("""
    <p>
        An AI-powered tool to help assess leukemia risk early — based on symptoms and blood test results.
        <br><br>
        Built for awareness, accessibility, and actionable health insights.
    </p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Call to action
st.markdown('<div class="btn-container">', unsafe_allow_html=True)
if st.button("🧪 Get Started"):
    st.switch_page("pages/symptoms_form.py")  # path
st.markdown('</div>', unsafe_allow_html=True)
