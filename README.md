# 📊Content-Monetization-Modeler 🎥💰

An end-to-end machine learning regression project in Social Media Analytics that predicts YouTube ad revenue (ad_revenue_usd) using video performance, engagement metrics, and contextual features. The project covers the full ML lifecycle and deploys the final model through a Streamlit web app for real-time revenue prediction 🚀

### Domain: 
Social Media Analytics
### Project Type: 
End-to-End Machine Learning Regression Project

### 📌 Project Overview
As video creators and media companies increasingly depend on platforms like YouTube for income, accurately predicting potential ad revenue is essential for business planning and content strategy.
This project builds a machine learning regression model to predict YouTube ad revenue (ad_revenue_usd) for individual videos based on performance and contextual features.
The final model is deployed using a Streamlit web application for interactive revenue prediction.

### 🎯 Problem Statement
Predict the daily YouTube ad revenue for a video using historical engagement, content characteristics, and contextual information.

### 💼 Business Use Cases

Content Strategy Optimization:
Identify content types that generate higher revenue.

Revenue Forecasting:
Estimate expected income from future video uploads.

Creator Analytics Tools:
Can be integrated into dashboards for YouTube creators.

Ad Campaign Planning:
Helps advertisers forecast ROI based on engagement metrics.

### 🏆 Key Results

Built and evaluated regression models to predict YouTube ad revenue (ad_revenue_usd).

Identified key revenue drivers including views, watch time, engagement rate, and subscribers.

Achieved strong model performance using R², RMSE, and MAE metrics.

Deployed the final model as an interactive Streamlit web application.

### 🛠️ Technologies Used

Python 3.x

Machine Learning: Scikit-learn

Data Analysis: Pandas, NumPy

Visualization: Matplotlib, Seaborn

Web App: Streamlit

Model Persistence: Joblib, Pickle

### 📂 Dataset Information

Dataset Name: YouTube Monetization Modeler

Format: CSV

Rows: ~122,000

Source: Synthetic (created for learning purposes)

Target Variable: ad_revenue_usd

### Features:
video_id: Unique identifier

date: Upload/report date

views, likes, comments: Performance metrics

watch_time_minutes, video_length_minutes: Engagement metrics

subscribers: Channel subscriber count

category, device, country: Contextual information

ad_revenue_usd: Revenue generated (target variable)

### 🔄 Project Workflow

### 1. Data Loading & Understanding

Inspect structure, datatypes, and target variable

### 2. Exploratory Data Analysis (EDA)

Distribution analysis

Correlation analysis

Trend & outlier detection

### 3. Data Preprocessing

Missing value handling

Duplicate removal

Categorical encoding

Outlier treatment

### 4. Feature Engineering

Engagement rate creation
(likes + comments) / views

Date-based features (day, month)

### 5. Model Building

Linear Regression

Ridge Regression

Lasso Regression

Random Forest Regressor

Gradient Boosting Regressor

### 6. Model Evaluation

R² Score

RMSE

MAE

### 7. Model Deployment

Interactive Streamlit application

### 📈 Model Evaluation Metrics

R² Score – Explained variance

RMSE – Penalizes large errors

MAE – Average prediction error

The final model was selected based on highest R² and lowest RMSE & MAE.

### 🌐 Streamlit Application Features

User input for video metrics

Real-time ad revenue prediction

Simple, intuitive UI

Model-driven insights

### 📁 Project Structure

                      Content_Monetization_Modeler/
                      │
                      ├── data/
                      │   └── youtube_monetization.csv
                      │
                      ├── notebook/
                      │   └── content_monetization.ipynb
                      │
                      ├── app.py
                      ├── model.pkl
                      ├── requirements.txt
                      └── README.md


### ▶️ How to Run the Project

1️⃣ Install dependencies
                   
                   pip install -r requirements.txt

2️⃣ Run Streamlit App

                   streamlit run app.py

