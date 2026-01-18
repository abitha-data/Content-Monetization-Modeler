import streamlit as st
import pandas as pd
import joblib
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Content Monetization Modeler",
    layout="wide",
    page_icon="💰"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>
body {background-color:#0e1117; color:#fff;}
.sidebar .sidebar-content {background-color:#1c1c24;}
h1, h2, h3, h4 { color: #F9FAFB !important; }
.stNumberInput label, .stSelectbox label {
    color: #E0E0E0 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🔮 Predict YouTube Ad Revenue")

# ---------------- LOAD MODEL ----------------
MODEL_PATH = "C:/Users/abith/OneDrive/Desktop/Content Monetization Modeler/linear_regression_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found. Check the path.")
    st.stop()

model = joblib.load(MODEL_PATH)

# Get exact feature names from trained model
model_features = model.feature_names_in_

# ---------------- CURRENCY MAP ----------------
currency_map = {
    "India": {"symbol": "₹", "rate": 83},
    "USA": {"symbol": "$", "rate": 1},
    "UK": {"symbol": "£", "rate": 0.78},
    "Canada": {"symbol": "C$", "rate": 1.35},
    "Australia": {"symbol": "A$", "rate": 1.5}
}

# ---------------- CONFIDENCE BAND FUNCTION ----------------
def revenue_band(pred, views, subscribers, engagement_rate):
    # Hard business rules
    if views < 5000 or subscribers < 1000:
        return "🔴 Low Revenue Potential"

    if engagement_rate < 0.02:
        return "🟡 Medium Revenue Potential"

    # Model-based thresholds
    if pred < 30000:
        return "🟡 Medium Revenue Potential"
    else:
        return "🟢 High Revenue Potential"

# ---------------- USER INPUT ----------------
st.subheader("📊 Enter Video Details")

category = st.selectbox(
    "Category",
    ["Entertainment", "Gaming", "Lifestyle", "Music", "Tech"]
)

device = st.selectbox(
    "Device",
    ["Mobile", "Desktop", "Tablet"]
)

country = st.selectbox(
    "Country",
    ["India", "USA", "UK", "Canada", "Australia"]
)

day_of_week = st.selectbox(
    "Day of Week (0 = Monday, 6 = Sunday)",
    list(range(7))
)

col1, col2, col3 = st.columns(3)

with col1:
    views = st.number_input(
        "Views (can be low or high)",
        min_value=0.0,
        value=500.0,      # default low value
        step=100.0        # small step
    )

    likes = st.number_input(
        "Likes",
        min_value=0.0,
        value=50.0,
        step=10.0
    )

with col2:
    comments = st.number_input(
        "Comments",
        min_value=0.0,
        value=10.0,
        step=5.0
    )

    watch_time_minutes = st.number_input(
        "Watch Time (minutes)",
        min_value=0.0,
        value=300.0,
        step=50.0
    )

with col3:
    video_length_minutes = st.number_input(
        "Video Length (minutes)",
        min_value=0.0,
        value=5.0,
        step=1.0
    )

    subscribers = st.number_input(
        "Subscribers",
        min_value=0.0,
        value=200.0,
        step=50.0
    )

# ---------------- FEATURE ENGINEERING (SAME AS TRAINING) ----------------
engagement_rate = (likes + comments) / (views if views != 0 else 1)

# ---------------- BUILD INPUT (MATCH df_enc EXACTLY) ----------------
input_data = dict.fromkeys(model_features, 0)

# Numeric features
input_data["views"] = views
input_data["likes"] = likes
input_data["comments"] = comments
input_data["watch_time_minutes"] = watch_time_minutes
input_data["video_length_minutes"] = video_length_minutes
input_data["subscribers"] = subscribers
input_data["engagement_rate"] = engagement_rate

# One-hot encoded categorical features
if f"category_{category}" in input_data:
    input_data[f"category_{category}"] = 1

if f"device_{device}" in input_data:
    input_data[f"device_{device}"] = 1

if f"country_{country}" in input_data:
    input_data[f"country_{country}"] = 1

if f"day_of_week_{day_of_week}" in input_data:
    input_data[f"day_of_week_{day_of_week}"] = 1

input_df = pd.DataFrame([input_data])

# ---------------- PREDICTION ----------------
if st.button("Predict"):
    try:
        prediction_usd = model.predict(input_df)[0]
        prediction_usd = max(0, prediction_usd)

        # Currency conversion
        currency = currency_map.get(country, {"symbol": "$", "rate": 1})
        converted_value = prediction_usd * currency["rate"]

        band = revenue_band(
                prediction_usd,
                views,
                subscribers,
                engagement_rate
            )

        st.success(
            f"💰 Predicted Ad Revenue: "
            f"{currency['symbol']}{converted_value:,.2f}"
        )

        st.markdown(f"### 📊 Confidence Band: **{band}**")

        if "Low" in band:
            st.warning("⚠️ Low monetization potential. Improve views and engagement.")
        elif "Medium" in band:
            st.info("📈 Medium performance. Scaling content can boost revenue.")
        else:
            st.success("🚀 High monetization potential. Excellent performance!")

    except Exception as e:
        st.error(f"Prediction error: {e}")
