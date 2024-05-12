from odoo import models, fields, api, _



class PatientTag(models.Model):
    _name        = 'patient.tag'
    _description = 'Patient Tag'

    name    = fields.Char(string='Name', required=True)
    active  = fields.Boolean(string='Active', default=True, copy=False) #atr copy false membuat field copy tidak terduplikasi dan sesuai nilai default
    color   = fields.Integer(string='Color')
    color_2 = fields.Char(string='Color 2')
    sequence = fields.Integer(string='Sequence')
    
    @api.returns('self', lambda value: value.id) #copy method syntax executed whenever duplicate record is pressed
    def copy(self, default=None): #copy method digunakan untuk mengatasi masalah duplikasi yang terhalangi sql constraint
        if default is None: 
            default = {} #making the default empty
            
        if not default.get('name'):
            default['name'] = self.name + " (copy)" #adding name + " (copy)" into name field, _("%s (copy)", self.name), overriding duplication name from copy method
        default['sequence'] = self.sequence + 1 #membuat sequence +1 agar lolos check sequence
        return super(PatientTag,self). copy(default)
    #penempatan inherit copy method sebelum constraint sangat penting agar dapat menduplikasi dgn overriding 
    
    
    _sql_constraints = [ #bentuk data list-tuple 
        ("name_unique", "unique(name, active)", "Tag has been created already."),
        ("check_sequence", "check(sequence > 0)", "Sequence number must be non zero positive integer number!") 
    ]
    #ooconst, arg pertama merupakan name bebas, arg kedua kw unique merupakan sintaks untuk mengecek (field_name) agar value dari (field_name) unik dan bisa lebih dari satu field
    #check untuk mengecek value dari (field_name) agar sesuai dengan kondisi,apabila record yang telah disimpan menyalahi kondisi maka constraint tidak tereksekusi
    