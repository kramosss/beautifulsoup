import sys
import os
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    input_file = sys.argv[1]

    b_to_blockquote = SoupReplacer("b", "blockquote")

    with open(input_file, 'r', encoding='utf-8') as file:
        file_content = file.read()

    file_extension = os.path.splitext(input_file)[1].lower()

    if file_extension == ".html":
        soup = BeautifulSoup(file_content, 'html.parser', replacer=b_to_blockquote)
    elif file_extension == ".xml":
        soup = BeautifulSoup(file_content, 'xml', replacer=b_to_blockquote)
    else:
        print("Unsupported file type.")
        sys.exit(1)

    output_file = ""
    if file_extension == ".html":
        output_file = "output.html"
    elif file_extension == ".xml":
        output_file = "output.xml"

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

if __name__ == "__main__":
    main()