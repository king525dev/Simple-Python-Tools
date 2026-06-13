from openpyxl import Workbook
import random

wb = Workbook()
ws = wb.active

ws.title = "Sales"

headers = [
     "Month",
     "Product",
     "Sales"
]

ws.append(headers)

months = [
     "Jan", "Feb", "Mar",
     "Apr", "May", "Jun"
]

products = [
     "Laptop",
     "Phone",
     "Tablet"
]

for month in months:

     for product in products:

          ws.append([
               month,
               product,
               random.randint(1000, 10000)
          ])

wb.save("salesData.xlsx")

print("Excel file created")