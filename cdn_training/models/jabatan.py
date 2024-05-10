from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Jabatan(models.Model):
    _name         = 'jabatan'
    _description  = 'Jabatan'
    
    name          = fields.Char(string='Titel Jabatan')
    jenis_jabatan = fields.Selection(string='Jenis Jabatan', selection=[('kepala', 'Kepala Lembaga'), ('wakil', 'Wakil Kepala Lembaga'),('staff','Staff Lembaga'),])
    description   = fields.Text(string='Keterangan')
    pejabat_id = fields.Many2one(comodel_name='instruktur', string='Pejabat',readonly=True)
    
    
    @api.constrains('jenis_jabatan')
    def _check_jenis_jabatan_constraints(self):
        for record in self:
            if record.jenis_jabatan == 'kepala':
                existing_kepala = self.search([('jenis_jabatan','=','kepala')])
                if len(existing_kepala) > 1 or (len(existing_kepala) == 1 and existing_kepala.id != record.id):
                    raise ValidationError ("Hanya boleh ada satu Kepala / Pimpinan Lembaga")
            elif record.jenis_jabatan == 'wakil':
                existing_wakil = self.search([('jenis_jabatan','=','wakil')])
                if len(existing_wakil) > 1 or (len(existing_wakil) == 1 and existing_wakil.id != record.id):
                    raise ValidationError ("Hanya boleh ada satu Wakil Lembaga")