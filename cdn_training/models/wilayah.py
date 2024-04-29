from odoo import models, fields, api



class RefProvinsi(models.Model):
    _name = 'ref.provinsi'
    _description = 'Ref Provinsi'

    name = fields.Char(string='Nama Provinsi', required=True)
    kode = fields.Char(string='Kode', required=True)
    singkatan = fields.Char(string='Singkatan')
    deskripsi = fields.Text(string='Deskripsi')
    kota_ids = fields.One2many(comodel_name='ref.kota', inverse_name='provinsi_id', string='Daftar Kota')


class RefKota(models.Model):
    _name = 'ref.kota'
    _description = 'Ref Kota'

    name = fields.Char(string='Nama Kota', required=True)
    kode = fields.Char(string='Kode', required=True)
    provinsi_id = fields.Many2one(comodel_name='ref.provinsi', string='Nama Provinsi')
    singkatan = fields.Char(string='Singkatan')
    deskripsi = fields.Text(string='Deskripsi')
    kecamatan_ids = fields.One2many(comodel_name='ref.kecamatan', inverse_name='kota_id', string='Nama Kecamatan')


class RefKecamatan(models.Model):
    _name = 'ref.kecamatan'
    _description = 'Ref Kecamatan'

    name = fields.Char(string='Nama Kecamatan', required=True)
    kode = fields.Char(string='Kode',required=True)
    kota_id = fields.Many2one(comodel_name='ref.kota', string='Nama Kota')
    deskripsi = fields.Text(string='Deskripsi')
    desa_ids = fields.One2many(comodel_name='ref.desa', inverse_name='kecamatan_id', string='Nama Desa')
    

class RefDesa(models.Model):
    _name = 'ref.desa'
    _description = 'Ref Desa'

    name = fields.Char(string='Nama Desa', required=True)
    kode = fields.Char(string='Kode', required=True)
    kecamatan_id = fields.Many2one(comodel_name='ref.kecamatan', string='Nama Kecamatan')    
    deskripsi = fields.Text(string='Deskripsi')
    
    

    
    
    
    

    
    
    
