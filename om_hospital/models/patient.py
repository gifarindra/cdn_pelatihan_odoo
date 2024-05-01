from odoo import models, fields, api


class HospitalPatient(models.Model): #table (postgres)/ models(odoo)  omod
    _name        = 'hospital.patient' #all lowercase with . for the space
    _description = 'Hospital Patient'
    _inherit     = ['mail.thread', 'mail.activity.mixin'] #inherit chatter

    name   = fields.Char(string='Name', tracking=True)   #fields ofc  #tracking the field with the chatter
    ref    = fields.Char(string='Reference', tracking=True)
    age    = fields.Integer('Age', tracking=True) #ofint
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),], tracking=True) #ofsel
    active = fields.Boolean(string='Active', default=True, tracking=True) #add the archive feature on the form view 