import os

# Path to the folder containing PDFs
pdf_directory = './orders'

# Start of the HTML list
html_list = ''

# Loop through the folder to find all PDF files
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        # Add the PDF to the HTML list
        html_list += f'<li><a href="{pdf_directory}/{filename}" target="_blank">{filename}</a></li>\n'

# Read the existing index.html file
with open('index.html', 'r+') as f:
    html_content = f.read()

    # Insert the updated HTML list inside <ul id="pdf-list">
    start_pos = html_content.find('<ul id="pdf-list">') + len('<ul id="pdf-list">')
    end_pos = html_content.find('</ul>', start_pos)
    new_html_content = html_content[:start_pos] + '\n' + html_list + html_content[end_pos:]

    # Overwrite the file with the updated content
    f.seek(0)
    f.write(new_html_content)
    f.truncate()
