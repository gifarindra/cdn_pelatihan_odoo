# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#impor model res.config.settings

from odoo import fields, models


class ResConfigSettings(models.TransientModel): #inherit model res.config settings untuk menambah field 
    _inherit = ['res.config.settings']

    cancel_days = fields.Integer(string='Cancel Days', config_parameter='om_hospital.cancel_days') #Model Transien TIDAK menyimpan record pada database!, atr config_parameter membuat model ini dapat menyimpan record pada database meskipun sebuah model transien dan menyimpannya pada ir.config_parameter
    