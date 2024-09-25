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

    # Find the existing PDF list to avoid duplicates
    existing_list_start = html_content.find('<ul id="pdf-list">') + len('<ul id="pdf-list">')
    existing_list_end = html_content.find('</ul>', existing_list_start)
    existing_html_list = html_content[existing_list_start:existing_list_end]

    # Create a set of existing filenames to avoid duplicates
    existing_files = set()
    for line in existing_html_list.splitlines():
        if 'href="' in line:
            existing_files.add(line.split('"')[1].split('/')[-1])

    # Generate new list without duplicates
    final_html_list = ''
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf') and filename not in existing_files:
            final_html_list += f'<li><a href="{pdf_directory}/{filename}" target="_blank">{filename}</a></li>\n'

    # Update the HTML content with the new list
    new_html_content = html_content[:existing_list_start] + '\n' + final_html_list + html_content[existing_list_end:]

    # Overwrite the file with the updated content
    f.seek(0)
    f.write(new_html_content)
    f.truncate()
