# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Lot', 'Move']
__metaclass__ = PoolMeta


class Lot:
    __name__ = 'stock.lot'
    manufacturer = fields.Many2One('party.party', 'Manufacturer', domain=[
            ('manufacturer', '=', True),
            ])


class Move:
    __name__ = 'stock.move'
    lot_manufacturer = fields.Function(fields.Many2One('party.party',
            'Lot Manufacturer'),
        'on_change_with_lot_manufacturer')

    @fields.depends('lot')
    def on_change_with_lot_manufacturer(self, name=None):
        return (self.lot.manufacturer.id if self.lot and self.lot.manufacturer
            else None)
