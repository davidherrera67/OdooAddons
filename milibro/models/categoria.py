# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Categoria(models.Model):
    _name = 'milibro.categoria'
    _description = 'Descripción de la editorial'

    name = fields.Char(string="Categoria", required=True)

