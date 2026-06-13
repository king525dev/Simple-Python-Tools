import streamlit as st
import pandas as pd

st.title("Sales Dashboard")

uploaded_file = st.file_uploader(
     "Upload Sales Spreadsheet",
     type=["xlsx"]
)

if uploaded_file:

     df = pd.read_excel(uploaded_file)

     # Print Raw Data
     st.write("Raw Data")

     st.dataframe(df)

     # Print Total Data
     total_sales = df["Sales"].sum()

     st.metric(
          "Total Sales",
          f"£{total_sales:,.0f}"
     )
     
     
     # Print Sales by month - line graph
     month_order = [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec"
     ]

     df["Month"] = pd.Categorical(
          df["Month"],
          categories=month_order,
          ordered=True
     )

     monthly_sales = (
          df.groupby("Month")["Sales"]
          .sum()
     )

     st.line_chart(monthly_sales)
     
     # Print Sales by month - bar chart
     
     product_sales = (
          df.groupby("Product")["Sales"]
          .sum()
     )

     st.bar_chart(product_sales)
     
     col1, col2, col3 = st.columns(3)

     # KPI cards
     with col1:
          st.metric(
               "Total Revenue",
               f"£{df['Sales'].sum():,.0f}"
          )

     with col2:
          st.metric(
               "Average Sale",
               f"£{df['Sales'].mean():,.0f}"
          )

     with col3:
          st.metric(
               "Largest Sale",
               f"£{df['Sales'].max():,.0f}"
          )