from odoo import models, fields, api

class InputJabatanWizard(models.TransientModel):
    _name = 'input.jabatan.wizard'
    _description = 'Input Jabatan Wizard'
    
    
    jabatan_id = fields.Many2one(comodel_name='jabatan', string='ID Jabatan')
    pejabat_id = fields.Many2one(comodel_name='instruktur', string='Nama Pejabat')
    
    def action_update_jabatan(self):
        self.pejabat_id.write({'jabatan_id': self.jabatan_id.id})
        self.jabatan_id.write({'pejabat': self.pejabat_id.id})

        return {
            'effect' :{
                'fadeout' : 'slow',
                'message' : 'Jabatan Berhasil Diupdate',
                'type' : 'rainbow_man',
            }
        }
    
    
