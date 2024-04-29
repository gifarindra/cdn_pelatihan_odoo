from odoo import models, fields, api

class TrainingCourse(models.Model):
    _name           = 'training.course'
    _description    = 'Training Course'

    name        = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
