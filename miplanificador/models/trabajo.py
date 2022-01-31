# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Trabajo(models.Model):
    _name = 'milibro.trabajo'
    _description = 'Trabajos'

    name = fields.Char(string="Trabajo realizado", required=True)
    fields.Float(string="Horas dedicadas",required=True)
