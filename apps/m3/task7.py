from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer
import os 
import sys 

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r', encoding='utf-8') as file:
        file_content = file.read()

    file_extension = os.path.splitext(input_file)[1].lower()

    def add_test_class(tag):
        if tag.name == 'p':
            attrs = dict(tag.attrs) if tag.attrs else {}
            attrs['class'] = ['test']
            return attrs
        return tag.attrs
    
    replacer = SoupReplacer(attrs_xformer=add_test_class)
    if file_extension == ".html":
        soup = BeautifulSoup(file_content, 'html.parser', replacer=replacer)
    elif file_extension == ".xml":
        soup = BeautifulSoup(file_content, 'xml', replacer=replacer)
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
