from odoo import models, fields, api



class PatientTag(models.Model):
    _name        = 'patient.tag'
    _description = 'Patient Tag'

    name    = fields.Char(string='Name', required=True)
    active  = fields.Boolean(string='Active', default=True)
    color   = fields.Integer(string='Color')
    color_2 = fields.Char(string='Color 2')
    sequence = fields.Integer(string='Sequence')
    
    
    _sql_constraints = [ #bentuk data list-tuple 
        ("name_unique", "unique(name, active)", "Tag has been created already."),
        ("check_sequence", "check(sequence > 0)", "Sequence number must be non zero positive integer number!") 
    ]
    #ooconst, arg pertama merupakan name bebas, arg kedua kw unique merupakan sintaks untuk mengecek (field_name) agar value dari (field_name) unik dan bisa lebih dari satu field
    #check untuk mengecek value dari (field_name) agar sesuai dengan kondisi,apabila record yang telah disimpan menyalahi kondisi maka constraint tidak tereksekusi
    