from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

class TestIterator:
    # Iteration over romeo and juliet where every Tag and NavigableString should be present
    def test_iterate_romeo_and_juliet(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        count = 0
        seen_tag_names = []
        seen_strings = []

        for node in soup:
            count += 1
            if isinstance(node, Tag):
                seen_tag_names.append(node.name)
            elif isinstance(node, NavigableString):
                seen_strings.append(str(node))

        assert count == len(seen_tag_names) + len(seen_strings)
        assert 'html' in seen_tag_names
        assert 'body' in seen_tag_names
        assert 'p' in seen_tag_names
    
    # Iteration over sites.xml where every Tag and NavigableString should be present
    def test_iterate_sites(self):
        with open("../../sites.xml") as file:
            xml_doc = file.read()
        soup = BeautifulSoup(xml_doc, "xml")
        count = 0
        seen_tag_names = []
        seen_strings = []

        for node in soup:
            count += 1
            if isinstance(node, Tag):
                seen_tag_names.append(node.name)
            elif isinstance(node, NavigableString):
                seen_strings.append(str(node))

        assert count == len(seen_tag_names) + len(seen_strings)
        assert 'row' in seen_tag_names

    # Iteration over emphasized.html where every Tag and NavigableString should be present
    def test_iterate_emphasized(self):
        with open("../../emphasized.html") as file:
            html_doc = file.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        count = 0
        seen_tag_names = []
        seen_strings = []
        for node in soup:
            count += 1
            if isinstance(node, Tag):
                seen_tag_names.append(node.name)
            elif isinstance(node, NavigableString):
                seen_strings.append(str(node))
        
        assert count == len(seen_tag_names) + len(seen_strings)
        assert 'em' in seen_tag_names

    # Iteration over log4j.xml where every Tag and NavigableString should be present
    def test_iterate_log4j(self):
        with open("../../log4j.xml") as file:
            xml_doc = file.read()
        soup = BeautifulSoup(xml_doc, "xml")

        count = 0
        seen_tag_names = []
        seen_strings = []
        for node in soup:
            count += 1
            if isinstance(node, Tag):
                seen_tag_names.append(node.name)
            elif isinstance(node, NavigableString):
                seen_strings.append(str(node))
        
        assert count == len(seen_tag_names) + len(seen_strings)
        assert 'appender' in seen_tag_names
        assert 'logger' in seen_tag_names

    # Iteration over act.html where every Tag and NavigableString should be present
    def test_iterate_act(self):
        with open("../../act.html") as file:
            html_doc = file.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        count = 0
        seen_tag_names = []
        seen_strings = []

        for node in soup:
            count += 1
            if isinstance(node, Tag):
                seen_tag_names.append(node.name)
            elif isinstance(node, NavigableString):
                seen_strings.append(str(node))

        assert count == len(seen_tag_names) + len(seen_strings)
        assert 'meta' in seen_tag_names
        assert 'title' in seen_tag_names
        assert 'style' in seen_tag_names
        assert 'Activities' in seen_strings


    

