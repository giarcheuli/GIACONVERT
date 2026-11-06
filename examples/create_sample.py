"""Generate synthetic input and HTML; run from any directory, without AI services."""
from pathlib import Path
import sys
from docx import Document

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from giaconvert import WordToHTMLConverter

folder = Path(__file__).resolve().parent
source = folder / 'sample.docx'
output = folder / 'sample.html'
doc = Document()
doc.core_properties.author = 'GIACONVERT synthetic example'
doc.core_properties.last_modified_by = 'GIACONVERT synthetic example'
doc.add_heading('Synthetic publishing request', 0)
doc.add_paragraph('Fictional example for conversion validation. No client or employer data.')
p = doc.add_paragraph('Acceptance: ')
p.add_run('preserve this bold text').bold = True
table = doc.add_table(rows=1, cols=2)
table.rows[0].cells[0].text = 'Requirement'
table.rows[0].cells[1].text = 'Expected result'
cells = table.add_row().cells
cells[0].text = 'DOCX table'
cells[1].text = 'HTML table contains this row'
doc.save(str(source))
if not WordToHTMLConverter().convert_docx_to_html(str(source), str(output)):
    raise SystemExit('Conversion failed')
html = output.read_text()
assert 'Synthetic publishing request' in html
assert '<table' in html and 'HTML table contains this row' in html
assert 'font-weight: bold' in html or '<strong>' in html or '<b>' in html
print('PASS: synthetic heading, table row and bold markup preserved')
