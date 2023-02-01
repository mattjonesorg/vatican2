from vatican2lib import DocumentEncoder, DocumentProcessor

from pprint import pprint

import json


x = DocumentProcessor(
    'https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19641121_lumen-gentium_en.html')

x.run()

print(json.dumps(x.document, cls=DocumentEncoder, ensure_ascii=False, indent=4))
