# -*- coding: utf-8 -*-
from __future__ import (unicode_literals, division, absolute_import, print_function)

__license__   = 'GPL 3'
__copyright__ = '2017, Leonardo Brondani Schenkel <leonardo@schenkel.net>'
__docformat__ = 'restructuredtext en'

import urllib

from PyQt5.Qt import QUrl
from contextlib import closing
from lxml import html

from calibre import browser
from calibre.gui2 import open_url
from calibre.gui2.store import StorePlugin
from calibre.gui2.store.basic_config import BasicStoreConfig
from calibre.gui2.store.search_result import SearchResult
from calibre.gui2.store.web_store_dialog import WebStoreDialog

if __name__ == '__main__':
    from lib import GenericStore, xpath, text
else:
    from calibre_plugins.lbschenkel_store_cdon_se.lib import GenericStore, xpath, text

class CdonStore(GenericStore):
    url                = 'https://cdon.se'
    search_url         = '{0}/search?q={1}&category_group_id=1794'

    def find_search_results(self, doc):
        return xpath(doc, '//*', 'search-results', '/ul/li')

    def parse_search_result(self, node):
        r = SearchResult()
        r.detail_item = text(node, '(.//a)[1]', '', '/@href')
        r.title       = text(node, './/h3', 'title')
        r.author      = text(node, './/*', 'name')
        r.price       = text(node, './/*[@class="product-price-wrapper"]//*', 'price')
        r.cover_url   = text(node, './/img', '', '/@data-src')
        return r

    def find_book_details(self, doc):
        return xpath(doc, '//*[@itemtype="http://schema.org/Product"]')[0]

    def parse_book_details(self, node):
        r = SearchResult()
        r.title     = text(node, './/*[@itemprop="name"]')
        r.author    = text(node, './/*[@itemprop="author"]')
        r.price     = text(node, './/*', 'price ')
        r.cover_url = text(node, './/img[@itemprop="image"]', '', '/@src')
        r.formats   = text(node, '//th[contains(., "Mediatyp")]/following-sibling::td[1]')
        r.drm       = r.formats
        return r

class CdonStorePlugin(StorePlugin):
    store = CdonStore()

    def search(self, query, max_results, timeout):
        return self.store.search(query, max_results, timeout)

    def get_details(self, result, timeout):
        return self.store.get_details(result, timeout)

    def open(self, parent, item, external):
        return self.store.open(self.name, self.gui, parent, item, external)

    def create_browser(self):
        return self.store.create_browser()


if __name__ == '__main__':
    import sys
    query   = ' '.join(sys.argv[1:])
    max     = 3
    timeout = 10

    store = CdonStore()
    for r in store.search(query, max, timeout):
        print(r)
        store.get_details(r, timeout)
        print(r)
        print('---')
