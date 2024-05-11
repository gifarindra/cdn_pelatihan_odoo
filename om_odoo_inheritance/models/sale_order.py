from odoo import models, fields, api



class SaleOrder(models.Model): #omodi snippet untuk model inheritance
    _inherit = 'sale.order'    #tanpa _name hanya _inherit dengan nama model yang diinherit

    def test(self):
        return