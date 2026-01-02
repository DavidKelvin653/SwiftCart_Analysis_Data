# 📊 Customer Retention & Revenue Insights Dashboard

This project is a **Streamlit dashboard** built with **Pandas** and **Plotly Express** to analyze customer retention, delivery performance, and revenue trends across different cities. It provides interactive visualizations and actionable insights for improving logistics and customer loyalty.

---

## 🚀 Features
- **Customer Retention Analysis**
  - Percentage of returning customers by city
  - Identification of cities with lowest retention (e.g., Abuja at 25%)

- **Delivery Performance**
  - Average delivery time per city
  - Impact of delivery time categories on customer retention

- **Revenue Insights**
  - Total revenue by city
  - Daily revenue trends across cities

- **Order Frequency**
  - Average number of orders per customer
  - Frequency distribution by delivery fee

- **Interactive Visualizations**
  - Bar charts, line charts, and trend plots using Plotly
  - Streamlit integration for easy exploration

---

## 📂 Project Structure
├── Data101.csv           # Dataset containing customer, order, and delivery details
├── app.py                # Streamlit application script
└── README.md             # Project documentation


---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/DavidKelvin653/customer-insights-dashboard.git
   cd customer-insights-dashboard
## install dependencies
    pip install -r requirements.txt

## run app
streamlit run app.py

## Open in browser

Navigate to http://localhost:8501