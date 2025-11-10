import sys
import pytest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

class TestSoupReplacer():
     # Uses the milestone 2 constructor to replace b tags with blockquote tags
     def test_b_to_blockquote(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()
        b_to_blockquote = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote)
        assert soup.find("blockquote") is not None
        assert soup.find("b") is None
        print(BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote).prettify())

     # Uses the milestone 2 constructor to replace div tags with section tags
     def test_div_to_section(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()
        div_to_section = SoupReplacer("div", "section")
        soup = BeautifulSoup(html_doc, "html.parser", replacer=div_to_section)
        assert soup.find("section") is not None
        assert soup.find("div") is None
        print(BeautifulSoup(html_doc, "html.parser",replacer=div_to_section).prettify())

     # Uses name_xformer to replace b tags with blockquote tags
     def test_name_xformer_b_to_blockquote(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()

        def bold_to_blockquote(tag):
            if tag.name == "b":
                return "blockquote"
            return tag.name

        b_to_blockquote = SoupReplacer(name_xformer=bold_to_blockquote)
        soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote)
        assert soup.find("blockquote") is not None
        assert soup.find("b") is None
        print(BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote).prettify())

     # Uses attrs_xformer to add class="test" to all p tags
     def test_attrs_xformer_remove_class_attr(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()

        def remove_class_attr(tag):
            if 'class' in tag.attrs:
                attrs = dict(tag.attrs)
                del attrs['class']
                return attrs
            return tag.attrs
        
        class_deleter = SoupReplacer(attrs_xformer=remove_class_attr)
        soup = BeautifulSoup(html_doc, "html.parser", replacer=class_deleter)
        for tag in soup.find_all():
            assert 'class' not in tag.attrs
        print(BeautifulSoup(html_doc, "html.parser", replacer=class_deleter).prettify())

     # Uses xformer to track all tag names encountered
     def test_xformer_track_tags(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()
        tracked_tags = []

        def track_tags(tag):
            tracked_tags.append(tag.name)

        tracker = SoupReplacer(xformer=track_tags)
        soup = BeautifulSoup(html_doc, "html.parser", replacer=tracker)
        assert len(tracked_tags) > 0
        assert 'b' in tracked_tags
        assert 'div' in tracked_tags
        print(f"Tracked tags: {set(tracked_tags)}")

     # Uses both name_xformer and attrs_xformer to change i tags to em tags and add class="emphasis" to em tags
     def test_combined_replacer(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()

        def i_to_em(tag):
            if tag.name == "i":
                return "em"
            return tag.name
        
        def add_emphasis_class(tag):
            if tag.name == "em":
                attrs = dict(tag.attrs)
                attrs['class'] = 'emphasis'
                return attrs
            return tag.attrs
        
        replacer = SoupReplacer(name_xformer=i_to_em, attrs_xformer=add_emphasis_class)
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)
        assert soup.find("i") is None 
        em_tags = soup.find_all("em")
        if em_tags:
            for em in em_tags:
                assert 'emphasis' in em.get('class', [])
        print(BeautifulSoup(html_doc, "html.parser", replacer=replacer).prettify())

     # Uses name_xformer to conditionally change div tags with an id attribute to section tags
     def test_name_xformer_conditional_on_attrs(self):
        with open("../../romeoAndJuliet.html") as file:
            html_doc = file.read()

        def transform_divs_with_id(tag):
            if tag.name == "div" and 'id' in tag.attrs:
                return "section"
            return tag.name

        replacer = SoupReplacer(name_xformer=transform_divs_with_id)
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)
        sections = soup.find_all("section")
        remaining_divs = soup.find_all("div")
        for div in remaining_divs:
            assert 'id' not in div.attrs
        print(BeautifulSoup(html_doc, "html.parser", replacer=replacer).prettify())
    
     # Uses xformer to collect the number of tags, tags with class attributes, and tags with id attributes
     def test_xformer_collect_tag_numbers(self):
         with open("../../romeoAndJuliet.html") as file:
             html_doc = file.read()

         tag_counts = {'total': 0, 'with_class': 0, 'with_id': 0}

         def collect_tag_numbers(tag):
             tag_counts['total'] += 1
             if 'class' in tag.attrs:
                 tag_counts['with_class'] += 1
             if 'id' in tag.attrs:
                 tag_counts['with_id'] += 1

         replacer = SoupReplacer(xformer=collect_tag_numbers)
         soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)
         assert tag_counts['total'] > 0
         assert tag_counts['with_class'] >= 0
         assert tag_counts['with_id'] >= 0
         print(f"Total tags: {tag_counts['total']}")
         print(f"Tags with class: {tag_counts['with_class']}")
         print(f"Tags with id: {tag_counts['with_id']}")