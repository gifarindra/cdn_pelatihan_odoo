from odoo import models, fields, api



class ResPartner(models.Model): #omod
    _inherit = 'res.partner'

    jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),])
    provinsi_id = fields.Many2one('ref.provinsi', string='Provinsi')
    kota_id = fields.Many2one('ref.kota', string='Kota')
    kecamatan_id = fields.Many2one('ref.kecamatan', string='Kecamatan')
    desa_id = fields.Many2one('ref.desa', string='Desa/Kelurahan')


