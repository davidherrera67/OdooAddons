# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Categoria(models.Model):
    _name = 'milibro.categoria'
    _description = 'Categorías'

    name = fields.Char(string="Nombre", required=True)
