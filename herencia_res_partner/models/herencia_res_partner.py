# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class herencia_res_partner(models.Model): 
    _inherit = "res.partner" 
    codigo = fields.Integer(string='codigo', required=True) 
 
    fecha_alta = fields.Datetime(string='fecha_alta', required=True) 
 
    fecha_baja = fields.Datetime(string='fecha_baja', required=False) 
 
    fecha_evaluacion = fields.Datetime(string='fecha_evaluacion', required=False) 
 
    numero_incidencias = fields.Integer(string='numero_incidencias', required=True) 
 
