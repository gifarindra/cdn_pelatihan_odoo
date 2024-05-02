from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Instruktur(models.Model):
    _name        = 'instruktur'
    _description = 'Instruktur'
    _inherits    = {'res.partner':'partner_id'}

    partner_id   = fields.Many2one(comodel_name='res.partner', string='Partner', required=True, ondelete='cascade')
    keahlian_ids = fields.Many2many(comodel_name='keahlian', string='Keahlian')
    jabatan_id = fields.Many2one(comodel_name='jabatan', string='Jabatan')
    jenis_jabatan = fields.Selection(string='Jenis', related='jabatan_id.jenis_jabatan')
    jabatan_staff = fields.Char(string='Nama Jenis Staff')
    
    def action_update_jabatan(self):
        self.jabatan_id.pejabat_id = self.id
        return True
                    

class Keahlian(models.Model):
    _name        = 'keahlian'
    _description = 'Keahlian'

    name         = fields.Char(string='Keahlian', required=True)
    


