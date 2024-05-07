from odoo import models, fields, api


class HospitalAppointment(models.Model): #table (postgres)/ models(odoo)  omod
    _name              = 'hospital.appointment' #all lowercase with . for the space
    _description       = 'Hospital Appointment'
    _inherit           = ['mail.thread', 'mail.activity.mixin'] #inherit chatter
    _rec_name          = 'patient_id' #_rec_name digunakan untuk model yang tidak memiliki native name field (biasanya digunakan untuk model yang dependen thd model lain) 

    patient_id         = fields.Many2one(comodel_name='hospital.patient', string='Patient') #many2one from hospital.patient model/table
    gender             = fields.Selection( related="patient_id.gender") #atribut selection tidak perlu disematkan asal field yang dijadikan relasi memiliki atribut tsb. related merupakan field readonly (bisa dijadikan False) dari sumber yang tidak akan diubah 
    appointment_time   = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date       = fields.Date(string='Booking Date',default=fields.Datetime.now) #format tanggal dapat diubah di settings, languages, en_US, dateformat
    ref                = fields.Char(string='Reference', help="Reference of the patient from the patient record.") #bisa diubah mjd readonly false #field python bisa diberi atr help sebagai penjelasan dari sebuah field
    prescription       = fields.Html(string='Prescription')
    priority           = fields.Selection(string='Priority', selection=[('0', 'Normal'), ('1', 'Low'),('2','High'),('3','Very High')]) #penambahan widget priority lewat views
    state              = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('in_consultation', 'In Consultation'), 
                                         ('done', 'Done'), ('cancel', 'Cancelled')], default="draft", required=True) #state merupakan spesial keyword untuk menambahkan status pada suatu record, required berguna agar tidak ada record dengan state = 0
    doctor_id          = fields.Many2one(comodel_name='res.users', string='Doctor', tracking=True) #Field many2one dengan model res.users(base model dari odoo(rumit))
    pharmacy_lines_ids = fields.One2many(comodel_name='appointment.pharmacy.lines', 
                                        inverse_name='appointment_id', string='Pharmacy Lines') #pembuatan one2many, onenya adalah appointment_id dan many adalah record-record dari sebuah field yang akan diasosiasikan dgn appointment_id (product.product)
    
    
    
    #api onchange berubah saat terjadi saving record berbeda dengan depends
    @api.onchange('patient_id')  # penggunaan onchange mirip dengan related field namun bisa digunakan untk mengubah data dengan menerapkan readonly false pd python dan force_save pada view form/tree/etc
    def _onchange_patient_id(self):
        self.ref     = self.patient_id.ref #mengisi field hospital.appointment.ref dengan record ref dari field hospital.patient.ref melewati field m2o patient_id
    
    
    def action_test(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Succesful!',
                'type'   : 'rainbow_man', #rainbow effect (?) widget
            }
        }
    
    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
    def action_done(self):
        for rec in self:
            rec.state = 'done'
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
    #penggunaan atr default cukup berguna untuk beberapa field, pahami kapan dan dimana penggunaannya!



class AppointmentPharmacyLines(models.Model):
    _name          = 'appointment.pharmacy.lines'
    _description   = 'Appointment Pharmacy Lines'
    
    product_id     = fields.Many2one(comodel_name='product.product', required=True) #menentukan field2 apa yang akan dimunculkan di field one2many, mengambil banyak record dari product.product yang akan diasosiasikan dengan appointment_id
    price_unit     = fields.Float(related="product_id.list_price") #membuat list_price related field dari model product via product_id
    qty            = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment') #appointment_id (m2o dari hotel appointment)yg akan dijadikan acuan one2many
    