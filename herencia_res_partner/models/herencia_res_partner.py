# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class herencia_res_partner(models.Model): 
    _inherit = "res.partner" 
    codigo = fields.Integer(string='codigo', required=True)
    fecha_alta = fields.Date('Fecha alta') 
 
