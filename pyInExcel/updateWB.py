import openpyxl;

# Load an existing Excel file
wb = openpyxl.load_workbook(“report.xlsx”);
sheet = wb.active;

# Modify a cell value
sheet[“A1”] = “Updated with Python”;

# Save the file
wb.save(“report_updated.xlsx”);