import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("salesData.xlsx")

# Table Preview
print("===== Preview =====")
print(df.head())

# Sum
print("\n===== Total Sales =====")
print(df["Sales"].sum());

# Mean
print("\n===== Average Sales =====")
print(df["Sales"].mean());

# Max
print("\n===== Highest Sale =====")
print(df["Sales"].max());

# Total sales grouped by product
print("\n===== Sales by Product =====")
sales_by_product = (
     df.groupby("Product")["Sales"]
     .sum()
)

print(sales_by_product)

# Total sales grouped by month
print("\n===== Sales by Month =====")

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

print(monthly_sales)

# Product sales bar chart
print("\n===== Sales Bar Chart =====")
sales_by_product.plot(
     kind="bar",
     title="Sales by Product"
)

plt.tight_layout()

barFigName = "productSales.png"

plt.savefig(
     barFigName
)

print(f"Figure saved as `{barFigName}`")

plt.show()

# Product sales line plot
print("\n===== Sales Line Chart =====")

monthly_sales.plot(
     kind="line",
     marker="o",
     title="Monthly Sales Trend"
)

plt.tight_layout()

lineFigName = "monthlySales.png"

plt.savefig(
     lineFigName
)

print(f"Figure saved as `{lineFigName}`")

plt.show()

# Full Sales Report
report = f"""
\n==================
FULL SALES REPORT
==================

Total Sales:
{df['Sales'].sum():,.0f}

Average Sale:
{df['Sales'].mean():,.2f}

Best Product:
{sales_by_product.idxmax()}

Best Month:
{monthly_sales.idxmax()}
"""

print(report)