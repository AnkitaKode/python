from fpdf import FPDF

# Create PDF content
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

title = "Module-3: [5L]"
content = """
Regular Languages, Regular Sets, Regular Expressions, Algebraic Rules for Regular Expressions

Arden's Theorem statement and proof [1L]

Constructing Finite Automata (FA) for given regular expressions, Regular string accepted by FA [2L]

Constructing Regular Expression for a given Finite Automata [1L]

Pumping Lemma of Regular Sets. Closure properties of regular sets [1L]
"""

# Add title and content to PDF
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt=title, ln=True, align='C')
pdf.ln(5)
pdf.set_font("Arial", size=12)
for line in content.strip().split('\n'):
    pdf.multi_cell(0, 10, line.strip())

# Save the PDF
pdf_path = "/mnt/data/Module_3_Regular_Languages.pdf"
pdf.output(pdf_path)
pdf_path

