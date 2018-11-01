from bs4 import BeautifulSoup
import helpers
import json
from pathlib import Path
import re
import requests

class FMACrawler:
    def __init__(self):
        pass

    def crawl_doc(self, row):
        """Process one doc.
        """
        filename = row.find('td', {'headers': 'th-1'}).text
        url = row.find('td', {'headers': 'th-2'})
        url_links = url.findChildren('a')
        if len(url_links) != 1: # try first column; there might be a link there
            url = row.find('td', {'headers': 'th-1'})
            url_links = url.findChildren('a')
            if len(url_links) == 1:
                filename = url.text
                url = url_links[0]['href']
            else:
                url = ''
        else:
            filename = url.text
            url = url_links[0]['href']

        # find out if url is html or pdf
        ending = ''
        if url.lower().find('html') >= 0:
            ending = '.html'
        elif url.lower().find('pdf') >= 0:
            ending = '.pdf'
        elif url.lower().find('txt') >= 0: # check this last; this is probably a HTML from eurlex
            ending = '.html'

        return {'filename': filename + ending, 'url': url}

    def download_doc(self, doc, folder):
        folder_path = Path(folder)
        helpers.create_folder_if_not_exists(folder_path)

        helpers.download_file(doc['url'], folder_path / helpers.case_name_to_folder(doc['filename']))

    def crawl_eu_docs(self, link):
        docs_dict = []

        html = helpers.crawl(link)
        table = html.find('table', {'id': 'document-list'})
        if not table:
            raise RuntimeError()

        table_rows = table.findChildren('tbody')[0]
        table_rows = table_rows.findChildren('tr')

        for row in table_rows:
            doc = self.crawl_doc(row)
            docs_dict.append(doc)
        
        return docs_dict