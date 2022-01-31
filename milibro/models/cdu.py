# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CDU(models.Model):
    _name = 'milibro.cdu'
    _description = 'Descripción de la CDU'

    name = fields.Char(string="codigo")
    description = fields.Char(string="Descripción")

    @api.model
    def name_get(self):
        lista = []
        for r in self:
            lista.append((r.id,r.name + "-" + r.description))
        return lista

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        filtro = args + ['|',('name',operator,name),('description',operator,name)]
        return super(CDU,self).search(filtro,limit=limit).name_get()