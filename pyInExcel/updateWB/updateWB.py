import openpyxl;
from openpyxl.styles import Font;
from openpyxl.chart import BarChart, Series, Reference

# Load an existing Excel file
wb = openpyxl.load_workbook('report.xlsx');
sheet = wb.active;

# Modify a cell value
sheet['A1'] = 'Updated with Python';

# Data Values
treeData = [["Type", "Leaf Color", "Height"], ["Maple", "Red", 549], ["Oak", "Green", 783], ["Pine", "Green", 1204]];

# Append Table
for row in treeData:
     sheet.append(row);
     
# Make Row Head Bold
ft = Font(bold=True)
for row in sheet["A2:C2"]:
     for cell in row:
          cell.font = ft

# Create Bar Chart Skeleton
chart = BarChart()
chart.type = "col"
chart.title = "Tree Height"
chart.y_axis.title = 'Height (cm)'
chart.x_axis.title = 'Tree Type'
chart.legend = None

# Get References
data = Reference(sheet, min_col=3, min_row=3, max_row=5, max_col=3)
categories = Reference(sheet, min_col=1, min_row=2, max_row=4, max_col=1)

chart.add_data(data)
chart.set_categories(categories)

sheet.add_chart(chart, "E1")

# Save the file
wb.save('report_updated.xlsx');