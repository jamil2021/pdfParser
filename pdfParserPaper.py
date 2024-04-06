from py_pdf_parser.loaders import load_file
from py_pdf_parser import tables

from py_pdf_parser.visualise import visualise


# Step 1 - Load the file
document = load_file("IJCNS20110900004_79507510.pdf")

# visualise(document)

# Step 2 - Use a font mapping

# Show all fonts:
# print(set(element.font for element in document.elements))

FONT_MAPPING = {
    'TimesNewRomanPS-BoldMT,12.0': "title",
    'TimesNewRomanPSMT,10.0': "sub_title",
    'TimesNewRomanPS-BoldMT,9.0': "text",
    'MMNCCB+SymbolMT,13.2': "table_header",
    'MMNCCB+SymbolMT,10.0': "table_text",
    'TimesNewRomanPS-ItalicMT,10.0': "abc1",
    'MMNCCB+SymbolMT,6.0': "abc2",
    'TimesNewRomanPSMT,8.0': "abc3",
    'TimesNewRomanPSMT,11.0': "abc4",
    'TimesNewRomanPS-BoldMT,8.0': "abc5",
    'TimesNewRomanPS-ItalicMT,6.0': "abc6",
    'TimesNewRomanPSMT,5.0': "abc7",
    'TimesNewRomanPSMT,9.0': "abc8",
    'TimesNewRomanPSMT,6.0': "abc9",
    'MMNCCB+SymbolMT,7.8': "abc10", 
    'TimesNewRomanPS-BoldMT,19.0': "abc11",
}

document = load_file("IJCNS20110900004_79507510.pdf", font_mapping=FONT_MAPPING)

# Step 3 - Add sections
order_summary_sub_title_element = (
    document.elements.filter_by_font("title")
    .filter_by_text_equal("Abstract")
    .extract_single_element()
)

print(order_summary_sub_title_element.text())