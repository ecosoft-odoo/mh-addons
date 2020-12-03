# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv


class promo_code(osv.osv):

    _name = "promo.code"
    _columns = {
        'product_id': fields.many2one('product.product', 'Product', ondelete='cascade', select=True),
        'promo_code': fields.char('Promo Code', size=64, required=True),
        'percent_commission': fields.float('Commission (%)', digits=(16, 2)),
        'promo_description': fields.char('Description', size=128),
    }
    _order = 'product_id'

promo_code()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
