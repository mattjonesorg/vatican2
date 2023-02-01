import vatican2lib
from vatican2lib import Document, DocumentEncoder, DocumentProcessor
import unittest


class TestDocument(unittest.TestCase):
    def test_constructor(self):
        doc = Document("Latin Title", "English Title", "Publish Date")
        self.assertEqual(doc.latin_title, "Latin Title")
        self.assertEqual(doc.english_title, "English Title")
        self.assertEqual(doc.publish_date, "Publish Date")
        self.assertListEqual(doc.chapters, [])


if __name__ == '__main__':
    unittest.main()
