from odoo import models, fields, api



class SaleOrder(models.Model): #omodi snippet untuk model inheritance
    _inherit = 'sale.order'    #tanpa _name hanya _inherit dengan nama model yang diinherit

    confirmed_user_id = fields.Many2one(comodel_name='res.users', string='Confirmed Users') #penambahan field baru pada model sale.order dari model res.users, perubahandpt dilihat di techn -> models -> fields -> misc
    