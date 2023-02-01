import vatican2lib
from vatican2lib import Document, DocumentEncoder, DocumentProcessor
import unittest


class TestDocumentProcessor(unittest.TestCase):

    def test_documentprocessor_lumen_gentium(self):
        url = 'https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19641121_lumen-gentium_en.html'

        docprocessor = vatican2lib.DocumentProcessor(url)
        self.assertEqual(docprocessor.url, url)
        docprocessor.run()
        self.assertEqual(docprocessor.document.english_title,
                         "DOGMATIC CONSTITUTION ON THE CHURCH")
        self.assertEqual(docprocessor.document.latin_title, "LUMEN GENTIUM")
        self.assertEqual(docprocessor.document.publish_date,
                         "NOVEMBER 21, 1964")
        self.assertEqual(len(docprocessor.document.chapters), 8)
