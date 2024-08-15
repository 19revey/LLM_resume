from html import escape

def convert_text_to_html(texts: list):
    """ Convert the list of text to HTML format

    Args:
        texts (list): List of text strings
    """
    # Convert the array of text to HTML format
    html_output = "<ul>\n"
    for text in texts:
        html_output += f"  <li>{escape(text)}</li>\n"
    html_output += "</ul>"
    
    return html_output

