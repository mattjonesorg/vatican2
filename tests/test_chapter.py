import vatican2lib
from vatican2lib import Document, DocumentEncoder, DocumentProcessor
import unittest


class TestChapter(unittest.TestCase):
    def test_constructor(self):
        chapter = vatican2lib.Chapter("I", "Chapter Title")
        self.assertEqual(chapter.roman_numeral, "I")
        self.assertEqual(chapter.title, "Chapter Title")
        self.assertDictEqual(chapter.paragraphs, {})
        self.assertEqual(chapter.number, 1)

    def test_add_paragraph(self):
        chapter = vatican2lib.Chapter("I", "Chapter Title")
        self.assertEqual(chapter.roman_numeral, "I")
        chapter.add_paragraph(1, "Paragraph 1")
        self.assertDictEqual(chapter.paragraphs, {1: "Paragraph 1"})
        chapter.add_paragraph(2, "Paragraph 2")
        self.assertDictEqual(chapter.paragraphs, {
                             1: "Paragraph 1", 2: "Paragraph 2"})

    def test_convert_roman_numeral_to_int(self):
        chapter = vatican2lib.Chapter("I", "Chapter Title")
        self.assertEqual(chapter.convert_roman_numeral_to_int("I"), 1)
        self.assertEqual(chapter.convert_roman_numeral_to_int("II"), 2)
        self.assertEqual(chapter.convert_roman_numeral_to_int("III"), 3)
        self.assertEqual(chapter.convert_roman_numeral_to_int("IV"), 4)
        self.assertEqual(chapter.convert_roman_numeral_to_int("V"), 5)
        self.assertEqual(chapter.convert_roman_numeral_to_int("VI"), 6)
        self.assertEqual(chapter.convert_roman_numeral_to_int("VII"), 7)
        self.assertEqual(chapter.convert_roman_numeral_to_int("VIII"), 8)
        self.assertEqual(chapter.convert_roman_numeral_to_int("IX"), 9)
        self.assertEqual(chapter.convert_roman_numeral_to_int("X"), 10)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XI"), 11)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XII"), 12)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XIII"), 13)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XIV"), 14)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XV"), 15)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XVI"), 16)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XVII"), 17)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XVIII"), 18)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XIX"), 19)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XX"), 20)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XXI"), 21)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XXII"), 22)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XXIII"), 23)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XXIV"), 24)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XXV"), 25)
        self.assertEqual(chapter.convert_roman_numeral_to_int("XXVI"), 26)

    def test_convert_roman_numeral_to_int_invalid(self):
        chapter = vatican2lib.Chapter("I", "Chapter Title")
        with self.assertRaises(ValueError):
            chapter.convert_roman_numeral_to_int("0")
            chapter.convert_roman_numeral_to_int("A")
