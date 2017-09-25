# -*- coding: utf-8 ts=4 sw=4 sts=4 et -*-
from __future__ import (absolute_import, print_function, unicode_literals)

__license__   = 'GPL 3'
__copyright__ = '2017, Leonardo Brondani Schenkel <leonardo@schenkel.net>'
__docformat__ = 'restructuredtext en'

from calibre.customize import StoreBase

class CdonStore(StoreBase):
    name            = 'CDON.se'
    version         = (0, 1, 0)
    description     = 'Nordens största varuhus'
    author          = 'Leonardo Brondani Schenkel <leonardo@schenkel.net>'
    actual_plugin   = 'calibre_plugins.lbschenkel_store_cdon_se.cdon:CdonStorePlugin'
    headquarters    = 'SE'
    formats         = ['EPUB', 'PDF']

