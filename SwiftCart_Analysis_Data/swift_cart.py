import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv("Data101.csv")
#print(df)

#Customer retention
Returning_customer = (df.groupby("city")["is_returning"].mean().mul(100).round(1).reset_index(name="% of customers returning"))
lcr=f'Abuja has the lowest returning customer rate(25%)'
#print(Returning_customer)
#print(lcr)

#Delivery Performance
Avg_delivery_time= (df.groupby("city")["delivery_time"].mean().round().reset_index(name="Avg Delivery_time per city"))
#print(Avg_delivery_time)

df["Delivery_time_category"]=pd.cut(
    df["delivery_time"],bins=(0,20,30,45,50,60,75,100),
    labels=("<20","20-29","30-44","45-49","50-59","60-74","75+")
)
Delivery_time_category = df.groupby("Delivery_time_category")["is_returning"].mean().mul(100).reset_index()
Delivery_time_category.columns = ["Delivery_time", "Retention_rate"]

#print(f'\n{Delivery_time_category}')

#print('Delivery Time affects Retention rate,\nLonng term Delivery affects customer retention rate')

#Revenue and Profit insight
City_revenue=(df.groupby("city")["order_value"].sum().reset_index(name="Total Revenue"))
#print(City_revenue)
#print('Lagos has the highest Total revenue')

order_frequency0=(df.groupby('delivery_fee')['customer_id'].size().reset_index(name='Order_frequency'))
#print(order_frequency)
daily_city['rolling_revenue'] = daily_city.groupby('city')['order_value'].transform(lambda x: x.rolling(7).mean())


#Order frequency
orders=df.groupby('customer_id')['order_id'].size().reset_index(name='No.of orders')
#print(orders)
total_orders=orders['No.of orders'].sum()
total_customers=orders['customer_id'].value_counts().sum()
order_frequency = total_orders/total_customers
#print(f'Order Frequency is {order_frequency} orders per customer')

fig1=px.bar(
    Returning_customer,
    x='city',
    y="% of customers returning",
    title='% Returning Customers in cities'
)
st.plotly_chart(fig1,use_container_width=True)

fig2=px.bar(
    Avg_delivery_time,
    x='city',
    y='Avg Delivery_time per city',
    title='Average Delivery time per city'   
)
st.plotly_chart(fig2,use_container_width=True)

fig3=px.line(
    Delivery_time_category,
    x='Delivery_time',
    y='Returning_customers',
    title='Delivery time affecting returning customers'
)
st.plotly_chart(fig3,use_container_width=True)

fig4=px.line(
    City_revenue,
    x='city',
    y='Total Revenue',
    title="Cities n' Revenues"
)
st.plotly_chart(fig4,use_container_width=True)

fig5=px.line(
    daily_city,
    x='order_date',
    y='order_value',
    color='city',
    title='Daily Revenue Trends by City'
)
st.plotly_chart(fig5,use_container_width=True)

st.write("""Conclusion :\nCities with faster delivery times tend to have higher returning customers and revenue.
         \nImproving delivery speed in Abuja could improve retention.""")
st.write("""o Optimize logistics in Abuja\no Maintain Lagos delivery standards\no 
         Target loyalty programs in PH""")

st.metric("Order Frequency", f"{order_frequency:.2f} orders per customer")
st.metric("Lowest Retention City", "Abuja (25%)")
