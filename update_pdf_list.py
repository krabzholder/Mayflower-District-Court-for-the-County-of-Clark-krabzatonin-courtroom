import os

# Path to the folder containing PDFs
pdf_directory = './orders'

# Start of the HTML list and the JavaScript array
html_list = ''
pdf_files_array = []

# Loop through the folder to find all PDF files
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        # Add the PDF to the HTML list
        html_list += f'<li><a href="{pdf_directory}/{filename}" target="_blank">{filename}</a></li>\n'
        pdf_files_array.append(f'"{filename}"')  # Add to the JS array

# Read the existing index.html file
with open('index.html', 'r+') as f:
    html_content = f.read()

    # Find the position of <ul id="pdf-list"> and update the list
    start_pos = html_content.find('<ul id="pdf-list">') + len('<ul id="pdf-list">')
    end_pos = html_content.find('</ul>', start_pos)

    # Insert the updated HTML list inside <ul id="pdf-list">
    new_html_content = html_content[:start_pos] + '\n' + html_list + html_content[end_pos:]

    # Remove the old pdfFiles array and add the new one
    new_html_content = new_html_content.replace(
        'const pdfFiles = [',
        f'const pdfFiles = [\n            {",\n            ".join(pdf_files_array)},\n'
    )

    # Overwrite the file with the updated content
    f.seek(0)
    f.write(new_html_content)
    f.truncate()
