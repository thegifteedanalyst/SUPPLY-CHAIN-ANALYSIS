import streamlit as st
import numpy as np
import pickle

with open("supplychain_model.pkl", "rb") as f:
    model = pickle.load(f)


# Preprocess
df['Festival'] = df['Festival'].fillna('No')
df = df.dropna(subset=[
    'Delivery_person_Ratings', 'Vehicle_condition', 'Road_traffic_density',
    'Weather_conditions', 'Time_taken (min)', 'City', 'Type_of_order'
])

st.set_page_config(page_title="Zomato Delivery Insights", layout="wide")
st.title("🚀 Zomato Delivery Performance Dashboard")
st.markdown("**Prepared by The Gifted Analyst**")

# KPI Section
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Deliveries", len(df))
with col2:
    st.metric("Avg. Delivery Time (min)", round(df['Time_taken (min)'].mean(), 2))
with col3:
    st.metric("Avg. Rider Rating", round(df['Delivery_person_Ratings'].mean(), 2))

st.markdown("---")

# Avg Delivery Time by City
st.subheader("Average Delivery Time by City")
avg_city = df.groupby("City")["Time_taken (min)"].mean().sort_values()
st.bar_chart(avg_city)

# Rating Impact
st.subheader("Delivery Time vs Rider Ratings")
avg_rating = df.groupby("Delivery_person_Ratings")["Time_taken (min)"].mean()
st.line_chart(avg_rating)

# Traffic Impact
st.subheader("Impact of Road Traffic on Delivery Time")
avg_traffic = df.groupby("Road_traffic_density")["Time_taken (min)"].mean()
st.bar_chart(avg_traffic)

# Festival Comparison
st.subheader("Delivery Time: Festival vs Non-Festival")
avg_festival = df.groupby("Festival")["Time_taken (min)"].mean()
st.bar_chart(avg_festival)

# Weather Impact
st.subheader("Delivery Time by Weather Conditions")
avg_weather = df.groupby("Weather_conditions")["Time_taken (min)"].mean()
st.bar_chart(avg_weather)

st.markdown("---")
st.caption("Powered by The Gifted Analyst | www.thegifteedanalyst.blog.com")
