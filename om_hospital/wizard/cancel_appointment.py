from odoo import models, fields, api


class CancelAppointmentWizard(models.TransientModel): #transient model dibutuhkan untuk pembuatan wizard (dan biasanya untuk tujuan lain dmn kita tidak perlu menyimpan data)
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
    
    def action_cancel(self):
        return