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
    'TimesNewRomanPS-BoldMT,12.0': "section_title",
    'TimesNewRomanPSMT,10.0': "normal_text",
    'TimesNewRomanPS-BoldMT,9.0': "figure_table_caption",
    'MMNCCB+SymbolMT,13.2': "unknown_text1",
    'MMNCCB+SymbolMT,10.0': "unknown_text2",
    'TimesNewRomanPS-ItalicMT,10.0': "authors_info",
    'MMNCCB+SymbolMT,6.0': "unknown_text3",
    'TimesNewRomanPSMT,8.0': "table_data",
    'TimesNewRomanPSMT,11.0': "keywords",
    'TimesNewRomanPS-BoldMT,8.0': "table_header",
    'TimesNewRomanPS-ItalicMT,6.0': "equation_in_normal_text",
    'TimesNewRomanPSMT,5.0': "zero1",
    'TimesNewRomanPSMT,9.0': "refs_plus_top_header",
    'TimesNewRomanPSMT,6.0': "subscript_maybe",
    'MMNCCB+SymbolMT,7.8': "unknown_text3", 
    'TimesNewRomanPS-BoldMT,19.0': "main_title",
}

document = load_file("IJCNS20110900004_79507510.pdf", font_mapping=FONT_MAPPING)

# Step 3 - Add sections
# for finding fonts associated with text elements one by one
# all the fonts labeled above are found using below contruct
# order_summary_sub_title_element = (
#     document.elements.filter_by_font("keywords")
# )

# for e in order_summary_sub_title_element:
#     print(e.text())
# # print(order_summary_sub_title_element)
    
# Step 3 - Add sections
abstract_element = (
    document.elements.filter_by_font("section_title")
    .filter_by_text_equal("Abstract")
    .extract_single_element()
)

# print(abstract_element.text())

keywords_element = (
    document.elements.filter_by_font("keywords")
    .filter_by_text_equal("Keywords: LEO, Satellite, Range, Horizon")
    .extract_single_element()
)

# introduction_title_element = (
#     document.elements.filter_by_font("title")
#     .filter_by_text_equal("1. Introduction")
#     .extract_single_element()
# )

# print(introduction_title_element.text())

abstract_section = document.sectioning.create_section(
    name="abstract",
    start_element=abstract_element,
    end_element=keywords_element,
    include_last_element=False,
)

# Iterate over elements in the section and extract their text
abstract_text = ""
for element in abstract_section.elements:
    abstract_text += element.text() + "\n"

# Print or save the extracted text
print("Abstract:\n", abstract_text)