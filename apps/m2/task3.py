from bs4 import BeautifulSoup, SoupStrainer
import sys 
import os 

if len(sys.argv) < 2:
    sys.exit(1)

input_file = sys.argv[1]

file_extension = os.path.splitext(input_file)[1].lower()

all_tags = SoupStrainer(True)

if file_extension == ".html":
    print(BeautifulSoup(open(input_file), "html.parser", parse_only=all_tags))
elif file_extension == ".xml":
    print(BeautifulSoup(open(input_file), "xml", parse_only=all_tags))