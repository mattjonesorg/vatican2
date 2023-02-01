import datetime
import decimal
import requests
import json
from bs4 import BeautifulSoup
from json import JSONEncoder


class DocumentProcessor:

    def __init__(self, url) -> None:
        self.url = url

    def run(self):
        self.data = requests.get(self.url)
        self.html = BeautifulSoup(self.data.text, 'html.parser')
        header_element = self.html.find('center')
        self.parse_header(header_element)
        self.parse_body()

    def parse_header(self, header_element):
        latin_title_element = header_element.find('b')
        latin_title = latin_title_element.text
        raw_text = header_element.find_all("font")[0].text
        publish_date = raw_text[raw_text.find("PAUL ")+len("PAUL VI ON"):]
        english_name = raw_text[:raw_text.find(latin_title)]
        self.document = Document(latin_title, english_name, publish_date)

    def parse_body(self):
        td = self.html.find('table', attrs={"width": "98%"}).find('td')
        found_header = False
        for child in td.children:
            if not found_header:
                if child.text.find(self.document.english_title):
                    found_header = True
            elif not self.is_element_blank(child):
                if self.is_chapter(child):
                    self.parse_chapter(child)
                else:
                    self.parse_paragraph(child.text)

    def parse_chapter(self, element):
        chapter_header = element.text.strip()
        header_parts = chapter_header.split()
        chapter_number = header_parts[1].strip()
        chapter_title = element.text.replace(
            "CHAPTER {0}".format(chapter_number), "").strip()
        chapter = Chapter(chapter_number, chapter_title)
        self.current_chapter = chapter
        self.document.add_chapter(chapter)

    def parse_paragraph(self, text):
        current_text = ''

    def is_element_blank(self, element):
        return element.name == 'br' or len(element.text) == 0

    def is_chapter(self, element):
        return element.text.find("CHAPTER") > 0


class Chapter:
    roman_numeral = ""
    title = ""
    paragraphs = dict()

    def __init__(self, roman_numeral, title) -> None:
        self.roman_numeral = roman_numeral
        self.title = title
        self.paragraphs = dict()


class Document:
    def __init__(self, latin_title, english_title, publish_date) -> None:
        self.english_title = english_title.strip()
        self.latin_title = latin_title.strip()
        self.publish_date = publish_date.strip()
        self.chapters = list()

    def add_chapter(self, new_chapter):
        if new_chapter is not None:
            self.chapters.append(new_chapter)


class DocumentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
