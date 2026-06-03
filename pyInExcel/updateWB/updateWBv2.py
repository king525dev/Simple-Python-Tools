"""
OpenPyXL Cookbook
=================

This script demonstrates many of the most useful OpenPyXL features:

✓ Create workbook
✓ Create worksheets
✓ Read/write cells
✓ Append data
✓ Fonts
✓ Colours
✓ Borders
✓ Alignment
✓ Number formats
✓ Row heights
✓ Column widths
✓ Formulas
✓ Tables
✓ Charts
✓ Conditional formatting
✓ Data validation
✓ Comments
✓ Hyperlinks
✓ Images
✓ Freeze panes
✓ Filters
✓ Merged cells
✓ Protection
✓ Workbook metadata
✓ Page setup

Optional:
     Add a logo.png file beside this script to test images.
"""

import openpyxl

from openpyxl import Workbook

from openpyxl.styles import (
     Font,
     PatternFill,
     Border,
     Side,
     Alignment
)

from openpyxl.chart import (
     BarChart,
     LineChart,
     PieChart,
     Reference
)

from openpyxl.comments import Comment

from openpyxl.drawing.image import Image

from openpyxl.worksheet.table import (
     Table,
     TableStyleInfo
)

from openpyxl.worksheet.datavalidation import DataValidation

from openpyxl.formatting.rule import (
     CellIsRule,
     ColorScaleRule
)

from openpyxl.worksheet.page import PageMargins


# =====================================================
# CREATE WORKBOOK
# =====================================================

wb = Workbook()

sheet = wb.active
sheet.title = "OpenPyXL Cookbook"


# =====================================================
# WORKBOOK METADATA
# =====================================================

wb.properties.creator = "Ore"
wb.properties.title = "OpenPyXL Cookbook"
wb.properties.subject = "Learning OpenPyXL"


# =====================================================
# BASIC CELL WRITING
# =====================================================

sheet["A1"] = "OpenPyXL Cookbook"

sheet["A2"] = "This workbook demonstrates major OpenPyXL features."


# =====================================================
# COMMENTS
# =====================================================

sheet["A1"].comment = Comment(
     "Created automatically using OpenPyXL",
     "Ore"
)


# =====================================================
# FONT STYLING
# =====================================================

sheet["A1"].font = Font(
     bold=True,
     size=18,
     color="FFFFFF"
)


# =====================================================
# CELL FILL COLOUR
# =====================================================

sheet["A1"].fill = PatternFill(
     fill_type="solid",
     start_color="4F81BD"
)


# =====================================================
# ALIGNMENT
# =====================================================

sheet["A1"].alignment = Alignment(
     horizontal="center"
)


# =====================================================
# MERGED CELLS
# =====================================================

sheet.merge_cells("A1:E1")


# =====================================================
# COLUMN WIDTHS
# =====================================================

sheet.column_dimensions["A"].width = 25
sheet.column_dimensions["B"].width = 20
sheet.column_dimensions["C"].width = 15


# =====================================================
# ROW HEIGHTS
# =====================================================

sheet.row_dimensions[1].height = 30


# =====================================================
# SAMPLE DATA
# =====================================================

data = [
     ["Tree", "Leaf Colour", "Height (cm)"],
     ["Maple", "Red", 549],
     ["Oak", "Green", 783],
     ["Pine", "Green", 1204],
     ["Birch", "Yellow", 645],
     ["Cedar", "Dark Green", 920]
]

start_row = 5

for row in data:
     sheet.append(row)


# =====================================================
# HEADER FORMATTING
# =====================================================

header_font = Font(
     bold=True,
     color="FFFFFF"
)

header_fill = PatternFill(
     fill_type="solid",
     start_color="4472C4"
)

for cell in sheet[5]:

     cell.font = header_font
     cell.fill = header_fill


# =====================================================
# BORDERS
# =====================================================

thin = Side(
     border_style="thin",
     color="000000"
)

border = Border(
     left=thin,
     right=thin,
     top=thin,
     bottom=thin
)

for row in sheet.iter_rows(
          min_row=5,
          max_row=10,
          min_col=1,
          max_col=3):

     for cell in row:
          cell.border = border


# =====================================================
# NUMBER FORMATS
# =====================================================

sheet["E5"] = "Price"

sheet["E6"] = 12.50
sheet["E7"] = 23.99
sheet["E8"] = 99.95

for cell in sheet["E6:E8"]:

     for c in cell:
          c.number_format = "£#,##0.00"


# =====================================================
# FORMULAS
# =====================================================

sheet["G5"] = "Formula Demo"

sheet["G6"] = 10
sheet["G7"] = 20

sheet["G8"] = "=SUM(G6:G7)"
sheet["G9"] = "=AVERAGE(G6:G7)"
sheet["G10"] = "=MAX(G6:G7)"


# =====================================================
# TABLES
# =====================================================

table = Table(
     displayName="TreeTable",
     ref="A5:C10"
)

style = TableStyleInfo(
     name="TableStyleMedium9",
     showFirstColumn=False,
     showLastColumn=False,
     showRowStripes=True,
     showColumnStripes=False
)

table.tableStyleInfo = style

sheet.add_table(table)


# =====================================================
# FREEZE PANES
# =====================================================

sheet.freeze_panes = "A6"


# =====================================================
# FILTERS
# =====================================================

sheet.auto_filter.ref = "A5:C10"


# =====================================================
# DATA VALIDATION
# =====================================================

sheet["J5"] = "Status"

validation = DataValidation(
     type="list",
     formula1='"Pending,Approved,Rejected"'
)

sheet.add_data_validation(validation)

validation.add("J6:J20")


# =====================================================
# CONDITIONAL FORMATTING
# =====================================================

red_fill = PatternFill(
     start_color="FF0000",
     end_color="FF0000",
     fill_type="solid"
)

sheet.conditional_formatting.add(
     "C6:C10",
     CellIsRule(
          operator="greaterThan",
          formula=["900"],
          fill=red_fill
     )
)


# =====================================================
# COLOUR SCALE
# =====================================================

sheet.conditional_formatting.add(
     "C6:C10",
     ColorScaleRule(
          start_type='min',
          start_color='FFAAAA',
          end_type='max',
          end_color='00AA00'
     )
)


# =====================================================
# HYPERLINKS
# =====================================================

sheet["L5"] = "OpenAI"

sheet["L5"].hyperlink = "https://openai.com"

sheet["L5"].style = "Hyperlink"


# =====================================================
# CHART DATA REFERENCES
# =====================================================

data_ref = Reference(
     sheet,
     min_col=3,
     min_row=5,
     max_row=10
)

category_ref = Reference(
     sheet,
     min_col=1,
     min_row=6,
     max_row=10
)


# =====================================================
# BAR CHART
# =====================================================

bar = BarChart()

bar.title = "Tree Heights"

bar.y_axis.title = "Height"

bar.x_axis.title = "Tree"

bar.add_data(
     data_ref,
     titles_from_data=True
)

bar.set_categories(category_ref)

sheet.add_chart(bar, "N2")


# =====================================================
# LINE CHART
# =====================================================

line = LineChart()

line.title = "Tree Heights Trend"

line.add_data(
     data_ref,
     titles_from_data=True
)

line.set_categories(category_ref)

sheet.add_chart(line, "N18")


# =====================================================
# PIE CHART
# =====================================================

pie = PieChart()

pie.title = "Tree Heights Distribution"

pie.add_data(
     data_ref,
     titles_from_data=True
)

pie.set_categories(category_ref)

sheet.add_chart(pie, "N34")


# =====================================================
# IMAGES
# =====================================================

try:

     img = Image("logo.png")

     img.width = 120
     img.height = 120

     sheet.add_image(img, "S2")

except FileNotFoundError:

     print(
          "logo.png not found. "
          "Skipping image demonstration."
     )


# =====================================================
# PAGE SETUP
# =====================================================

sheet.page_setup.orientation = "landscape"

sheet.page_margins = PageMargins(
     left=0.5,
     right=0.5,
     top=0.75,
     bottom=0.75
)


# =====================================================
# SHEET PROTECTION
# =====================================================

sheet.protection.sheet = True
sheet.protection.password = "password123"


# =====================================================
# SAVE WORKBOOK
# =====================================================

wb.save("openpyxl_cookbook.xlsx")

print("Workbook created successfully!")