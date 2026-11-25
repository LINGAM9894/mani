from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Helvetica", style="B", size=18)
pdf.cell(0, 12, "Monthly Expense Summary", new_x="LMARGIN", new_y="NEXT")

# Body text
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(
    0,
    8,
    "Here is a quick overview of estimated monthly household expenses in INR.",
)
pdf.ln(6)

# Table header
pdf.set_font("Helvetica", style="B", size=11)
pdf.cell(100, 10, "Category", border=1)
pdf.cell(50, 10, "Amount (INR)", border=1, new_x="LMARGIN", new_y="NEXT")

# Table rows
pdf.set_font("Helvetica", size=11)
rows = [
    ("Groceries", "8,500"),
    ("Electricity & Internet", "2,400"),
    ("Commute", "3,200"),
]

for category, amount in rows:
  pdf.cell(100, 10, category, border=1)
  pdf.cell(50, 10, amount, border=1, new_x="LMARGIN", new_y="NEXT")

pdf.output("expense_summary.pdf")
print("Saved expense_summary.pdf")