import sys
import pytest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

class TestSoupReplacer():
     def test_b_to_blockquote(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()
        b_to_blockquote = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote)
        assert soup.find("blockquote") is not None
        assert soup.find("b") is None
        print(BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote).prettify())

     def test_div_to_section(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()
        div_to_section = SoupReplacer("div", "section")
        soup = BeautifulSoup(html_doc, "html.parser", replacer=div_to_section)
        assert soup.find("section") is not None
        assert soup.find("div") is None
        print(BeautifulSoup(html_doc, "html.parser",replacer=div_to_section).prettify())
