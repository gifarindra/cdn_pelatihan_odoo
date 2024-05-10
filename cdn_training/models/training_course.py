from odoo import models, fields, api
from datetime import timedelta

class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Table Training Course'

    name = fields.Char(string='Nama Kursus', required=True)
    description = fields.Text(string='keterangan')
    user_id = fields.Many2one(comodel_name='res.users', string='Penanggung Jawab')
    session_line = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Session') 
    product_ids = fields.Many2many(comodel_name='product.product', string='Peralatan/Konsumsi', domain=[('product_training','!=', 'non_training')])
    
    _sql_constraints = [
        ("name_course_unique", "Unique(name)", "Nama kursus sudah ada!"),
    ]


class TrainingSession(models.Model):
    _name        = 'training.session'
    _description = 'Training Session'
    _inherit     = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Session Name', required=True, tracking=True)
    course_id = fields.Many2one(comodel_name='training.course', string='Course Name', required=True, ondelete='cascade', tracking=True)
    start_date = fields.Date(string='Start Date', required=True , tracking=True)
    duration = fields.Float(string='Duration', required=True, tracking=True)
    seats = fields.Integer(string='Seats', tracking=True)
    instruktur_id = fields.Many2one(comodel_name='instruktur', string='Instructor Name', tracking=True)
    alamat = fields.Char(string='Alamat', related='instruktur_id.street', tracking=True)
    no_hp = fields.Char(string='No HP', related='instruktur_id.mobile', tracking=True)
    email = fields.Char(string='Email', related='instruktur_id.email', tracking=True)
    jenis_kel = fields.Selection(related='instruktur_id.jenis_kel', tracking=True)
    peserta_ids = fields.Many2many(comodel_name='peserta', string='Peserta', tracking=True)
    jml_peserta = fields.Integer(compute='_compute_jml_peserta', string='Jumlah Peserta', tracking=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('progress', 'Sedang Berlangsung'),('done','Selesai')], default="draft", tracking=True)
    end_date = fields.Date(string='End Date', compute="_compute_end_date", tracking=True)
    
    
    
    
    
    @api.depends('peserta_ids')
    def _compute_jml_peserta(self):
        for rec in self:
            rec.jml_peserta = len(rec.peserta_ids)

    def action_confirm(self):
        self.state = 'progress'
    
    def action_done(self):
        self.state= 'done'
    
    def action_draft(self):
        self.state = 'draft'

    @api.depends('start_date','duration')
    def _compute_end_date(self):
        for record in self:
            record.end_date = record.start_date + timedelta(days=record.duration)
    
    

