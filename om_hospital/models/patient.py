from odoo import models, fields, api
from datetime import date


class HospitalPatient(models.Model): #table (postgres)/ models(odoo)  omod
    _name        = 'hospital.patient' #all lowercase with . for the space
    _description = 'Hospital Patient'
    _inherit     = ['mail.thread', 'mail.activity.mixin'] #inherit chatter dari mail

    name   = fields.Char(string='Name', tracking=True)   #fields ofc  #tracking the field with the chatter
    date_of_birth = fields.Date(string='Date of Birth')
    ref    = fields.Char(string='Reference', tracking=True)
    age    = fields.Integer(string='Age', tracking=True, compute='_compute_age') #ofint #computed fields
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),], tracking=True, default='male') #ofsel
    active = fields.Boolean(string='Active', default=True, tracking=True) #add the archive feature on the form view 
    
    
    #computed fields merupakan readonly field yang memiliki depedensi thd field lain (BUKAN RELATED FIELD) dan tidak menerima input scr manual
    #computed field dieksekusi setelah ada action save tanpa api depends
    #jika age dijadikan computed field, maka field age dibuat dalam postgres setelah dob diberi value maka filtering berdasarkan computed field tdk dpt dilakukan
    @api.depends('date_of_birth') #sebuah dekorator api untuk membuat compute function berfungsi segera setelah ada perubahan thd dob, bukan saat saving
    def _compute_age(self):
        for rec in self: # iterasi dilakukan karena field yang akan dicompute dimiliki oleh banyak record agar tdk terjadi singleton error
            today = date.today() # memanggil fungsi today() dari modul py date dengan variable today
            if rec.date_of_birth: #mengambil tahun dari field dob jika field dob ada value
                rec.age = today.year - rec.date_of_birth.year # membuat field age menjadi tahun skrg - tahun dob
            else:
                rec.age = 0 # apabila tdk ada value di dob maka age = 0
        