from odoo import models, fields, api, _
import datetime
from odoo.exceptions import ValidationError
from datetime import date
from dateutil import relativedelta

class CancelAppointmentWizard(models.TransientModel): #transient model dibutuhkan untuk pembuatan wizard (dan biasanya untuk tujuan lain dmn kita tidak perlu menyimpan data)
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'
    
    @api.model #dekorator untuk default_get function untuk default_get function
    def default_get(self, fields):  #default_get function terpanggil saat mengklik wizard transientmodel
        res = super(CancelAppointmentWizard, self).default_get(fields)  #function ini akan memanggil default value yang ditetapkan dalam bentuk dictionary field:value
        res['date_cancel'] = datetime.date.today() #pemanggilan res dengan key (field_name) dan penetapan value baru dengan overriding 
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id') #default value dari appointment_id menggunakan orm method dan ambil active_id
        return res
        #inheriting default_get() must be placed before anything else within the code
        #overriding field dengan function dari modul bawaan python datetime dgn class datetime method today
        #variabel fields berisi list field2 yang telah didefinisi, variable res merupakan dictionary dari field yang telah diberi default value
        

    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment', domain=[('state','=','draft'),('priority','in',('0','1', False))]) #filtering menggunakan atr domain dpt dilakukan pada sisi py atau xml, domain filter mempunyai sintaks list-tuple, '|' sebelum tuple pertama menandakan operasi or diberlakukan untuk domain
    reason = fields.Text(string='Cancellation Reason') #field text mempunyai bidang yang lebih luas dan dapat diubah ukuran dimensinya shg lbh cocok apabila mempunyai informasi yang banyak
    date_cancel = fields.Date(string='Cancellation Date')
    
    
    def action_cancel(self): 
        cancel_day        = self.env['ir.config_parameter'].get_param('om_hospital.cancel_days') #ambil config parameter dengan key om_hospital.cancel_days
        allowed_date      = self.appointment_id.booking_date - relativedelta.relativedelta(days=int(cancel_day)) #typecast string to int
        if allowed_date < date.today(): #mengecek apabila allowed date kurang dari tanggal hari ini
            raise ValidationError (_('Sorry, you are only allowed to cancel maximum 5 days before your booking date.')) #raise validation error jika if dipenuhi dengan string error
        self.appointment_id.state = 'cancel'
        return {
            'type': 'ir.actions.client', #kedua baris ini penting untuk mereload halaman saat button dipencet
            'tag' : 'reload', 
        }