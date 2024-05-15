from odoo import models, fields, api, _



class HospitalOperation(models.Model):
    _name        = 'hospital.operation'
    _description = 'Hospital Operation'
    _log_access  = False #membuat field bawaan create_date, create_uid, write_date, Write_uid dihilangkan, tidak bisa digunakan pada model transien

    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor')
    operation_name = fields.Char(string='Operation Name')
    # reference_record = fields.Reference(string='Record')
    reference_record = fields.Reference(selection=[('hospital.patient','Patient'), ('hospital.appointment','Appointment')],string='Record') #Perlu ada selection (bentuk list-tuple) disini dimana saat string 'Patient' dipilih maka record pada hospital.patient akan muncul
    #Reference field stores data in string data type (model_name, id) meanwhile m2o field stores in integer 
    #jika sebuah model tdk punya _rec_name atau tech field name maka pembuatan record dari field m2o ke model ini tidak akan tercatat
    
    @api.model #dekorator diberikan untuk name create model yang tidak ada rec_name atau name field
    def name_create(self, name): #fungsi create_name tereksekusi saat ada pemberian value dimana relasi comodelnya tdk ada _rec_name atau kw name field 
        return self.create({'operation_name': name}).name_get()[0] #value name didapat saat user memberikan value pd field m2o selain model ini
    
    #jika ada rec_name dan name fungsi ini jg masih berguna untuk memberikan value ke field tertentu!!