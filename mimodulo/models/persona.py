# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Persona(models.Model):
    _name = 'mimodulo.persona'
    _description = 'Descripción del modelo Persona'

    name = fields.Char(string="Nombre",required=True, help=("Escribe tu nombre"))
    apellidos = fields.Char(string="Apellidos", required=True, help=("Escribe tus apellidos"))
    fecha_nacimiento=fields.Date(string="Fecha de Nacimiento")
    observaciones = fields.Text(string="Observaciones")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100