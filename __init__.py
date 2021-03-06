# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .stock import *


def register():
    Pool.register(
        Lot,
        Move,
        module='stock_lot_manufacturer', type_='model')
