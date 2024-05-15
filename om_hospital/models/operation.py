from odoo import models, fields, api, _



class HospitalOperation(models.Model):
    _name        = 'hospital.operation'
    _description = 'Hospital Operation'
    _log_access  = False #membuat field bawaan create_date, create_uid, write_date, Write_uid dihilangkan, tidak bisa digunakan pada model transien

    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor')
    