from odoo import models, fields, api


class HospitalAppointment(models.Model): #table (postgres)/ models(odoo)  omod
    _name        = 'hospital.appointment' #all lowercase with . for the space
    _description = 'Hospital Appointment'
    _inherit     = ['mail.thread', 'mail.activity.mixin'] #inherit chatter

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient') #many2one from hospital.patient model/table
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date',default=fields.Datetime.now) #format tanggal dapat diubah di settings, languages, en_US, dateformat
    
    
    
    
    