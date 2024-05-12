from odoo import models, fields, api
from datetime import date


class HospitalPatient(models.Model): #table (postgres)/ models(odoo)  omod
    _name          = 'hospital.patient' #all lowercase with . for the space
    _description   = 'Hospital Patient'
    _inherit       = ['mail.thread', 'mail.activity.mixin'] #inherit chatter dari mail

    name           = fields.Char(string='Name', tracking=True)   #fields ofc  #tracking the field with the chatter field dgn nama "name" merupakan special syntax untuk memunculkan nama sbg name field
    date_of_birth  = fields.Date(string='Date of Birth') #sumber computed field age
    ref            = fields.Char(string='Reference', tracking=True)
    age            = fields.Integer(string='Age', tracking=True, compute='_compute_age') #ofint #computed fields
    gender         = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),], tracking=True, default='male') #ofsel
    active         = fields.Boolean(string='Active', default=True, tracking=True) #add the archive feature on the form view 
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointments')
    image          = fields.Image(string='Image')
    tag_ids        = fields.Many2many(comodel_name='patient.tag', string='Patient Tags') #penjelasan lengkap mengenai mekanisme many2many bisa dilihat di odoomates 15 tutorial vid 57
    
    @api.model #perlu diberikan saat menginherit method (hanya create method saja??) dari model
    def create(self, vals): #oocreate snippet, untuk menginherit create method dari Models, ooverride snippet untuk override create method
        vals['ref'] = 'OMTEST' #Penetepan value dari field juga dapat dilakukan secara implisit lewat inherit create method dengan mengambil field 'ref' dan menetapkannya thdp suatu nilai (dalam hal ini string OMTEST), nilai OMTEST akan menimpa nilai dari ref jk dibuat dari form view
        return super(HospitalPatient, self). create(vals) #function/method inheritance dari create() menggunakan super funct, arg vals berisi field2 yang telah dibuat pada model, return perlu diberikan
        #tipe struktur data dari variabel vals adalah dictionary dengan key = field dan value = value_field
    
    
    @api.depends('date_of_birth') #sebuah dekorator api untuk membuat compute function berfungsi segera setelah ada perubahan thd dob, bukan saat saving
    def _compute_age(self):
        for rec in self: # iterasi dilakukan karena field yang akan dicompute dimiliki oleh banyak record agar tdk terjadi singleton error
            today = date.today() # memanggil fungsi today() dari modul py date dengan variable today
            if rec.date_of_birth: #mengambil tahun dari field dob jika field dob ada value
                rec.age = today.year - rec.date_of_birth.year # membuat field age menjadi tahun skrg - tahun dob
            else:
                rec.age = 1 # apabila tdk ada value di dob maka age = 0
    #computed fields merupakan readonly field yang memiliki depedensi thd field lain (BUKAN RELATED FIELD) dan tidak menerima input scr manual
    #computed field dieksekusi setelah ada action save tanpa api depends
    #jika age dijadikan computed field, maka field age dibuat dalam postgres setelah dob diberi value maka filtering berdasarkan computed field tdk dpt dilakukan