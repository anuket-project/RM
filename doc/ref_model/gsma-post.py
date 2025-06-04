from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_repeat_table_headers(docx_path, output_path):
    doc = Document(docx_path)

    for table in doc.tables:
        if len(table.rows) > 0:
            first_row = table.rows[0]
            #print(f"Handling row {table.rows[0]}")
            # Set heading format in the higher-level API (not always sufficient)
            first_row._tr.get_or_add_trPr()
            trPr = first_row._tr.trPr
            tblHeader = OxmlElement('w:tblHeader')
            trPr.append(tblHeader)

    doc.save(output_path)
    print(f"Saved modified document to: {output_path}")

if __name__ == "__main__":
    docx_path = "gsma/rm-intermediate.docx"
    output_path = "gsma/rm.docx"

    print(f"Adjusting table styles in {docx_path} to preserve table headers in new pages and saving the result to {output_path}")

    set_repeat_table_headers(docx_path, output_path)