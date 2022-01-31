# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ejemplar(models.Model):
    _name = 'milibro.ejemplar'
    _description = 'Descripción del modelo ejemplar'

    name = fields.Char(string="Código", compute="_añadir_ceros")
    situacion = fields.Boolean(string="Disponible", requiered=True)
    estado = fields.Selection([('1', "Bueno"), ('2', "Regular"), ('3', "Malo")], string="Estado de conservación",
                              required=True)
    libro_id = fields.Many2one(comodel_name="milibro.libro",string="Libro",required=True) #Un ejemplar tendra un libro

    @api.depends("create_date")
    def _añadir_ceros(self):
        for i in self:
            idZ=str(i.id)
            i.name = idZ.zfill(13)
